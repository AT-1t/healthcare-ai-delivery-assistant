"""Run with: streamlit run app.py"""
import streamlit as st
from healthcare_ai.core import SearchIndex, chunk_document, extract_text
from healthcare_ai.assistant import answer

st.set_page_config(page_title='Healthcare AI Research Assistant', page_icon='📚', layout='wide')
st.title('Healthcare AI Research Assistant')
st.caption('Portfolio prototype · Literature research only · Not medical advice · No patient data')
st.warning('Use public, non-sensitive documents only. Do not upload PHI, confidential client files, or patient records.')
files = st.file_uploader('Upload research PDFs or UTF-8 text files (8 MB each, up to 80 PDF pages)',
                         type=['pdf', 'txt'], accept_multiple_files=True)
question = st.text_input('Ask a research question', placeholder='What do these documents say about EGFR mutations?')
use_claude = st.checkbox('Generate a cited synthesis with Claude (requires ANTHROPIC_API_KEY)', value=False)
top_k = st.slider('Number of evidence passages', 1, 8, 4)
if st.button('Search evidence', type='primary'):
    if not files:
        st.info('Upload at least one research document first.')
    elif not question.strip():
        st.info('Enter a question first.')
    else:
        passages = []
        for f in files:
            try:
                text = extract_text(f.name, f.getvalue())
                if not text.strip():
                    st.warning(f'{f.name}: no extractable text (scanned PDFs require OCR).')
                    continue
                passages.extend(chunk_document(f.name, text))
            except Exception as exc:
                st.error(f'Could not read {f.name}: {exc}')
        if passages:
            hits = SearchIndex(passages).search(question, top_k=top_k)
            try:
                with st.spinner('Preparing answer...'):
                    st.markdown(answer(question, hits, use_claude=use_claude))
            except Exception as exc:
                st.error(f'Answer generation failed: {exc}')
            with st.expander('Evidence and relevance scores', expanded=True):
                for hit in hits:
                    st.markdown(f'**{hit.passage.document} · chunk {hit.passage.chunk_id}** — relevance {hit.score:.3f}')
                    st.write(hit.passage.text)
