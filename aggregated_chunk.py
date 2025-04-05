from cat.mad_hatter.decorators import hook,plugin
from langchain.docstore.document import Document

from cat.log import log


@hook
def after_rabbithole_splitted_text(chunks, cat):

    #create list o concatenated chunks
    concatenated_chunks_list = []

    
    #load settings and set n° of chunk to aggregrate in order to find the correct tag of each chunk without forget the context
    settings = cat.mad_hatter.get_plugin().load_settings()

    n_of_chunks = settings["n_of_chunks"]

    for i in range(0, len(chunks), n_of_chunks):
        # Select each chunk group
        chunk_group = chunks[i:i + n_of_chunks]
        # Concatenates the chunks
        concatenated_content = ''.join(chunk.page_content for chunk in chunk_group)
        concatenated_chunks_list.append(concatenated_content)        
        concatenated_new_document = Document(page_content=concatenated_content)
        chunks.append(concatenated_new_document)
    return chunks
