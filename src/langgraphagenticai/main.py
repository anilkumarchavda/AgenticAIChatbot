import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit

def load_langgraph_agenticai_app():
    """ 
    Load and run the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while implementing exception handling for roubustness.

    """

    ui = LoadStreamlitUI()

    user_input =ui.load_streamlit_ui()

    if not user_input:
        st.error("Error : Failes to load user input from the User Interface")
        return
    
    user_message = st.chat_input("Ask Anything...")

    if user_message:
        try:
            llm_config = GroqLLM(user_controls_input=user_input)
            model = llm_config.get_llm_model()
            #print(model)
            #print(llm_config)

            if not model:
                st.error("Error : LLM model could not be initialized")
                return
            
            usecase = user_input.get("selected_usecase")
            if not usecase:
                st.error("Error: No use case selected.")
                return
        
            print("g0")
            graph_builder = GraphBuilder(model=model)

            try:
                print("g1")
                graph= graph_builder.setup_graph(usecase)
                print(user_message)
                DisplayResultStreamlit(usecase=usecase,graph=graph, user_message=user_message).display_result_on_ui()
                print("g4")
            except Exception as e:
                st.error(f"Error : Graph setup failed - {e}")


        except Exception as e:
            st.error(f"Error: Graph setup failed - {e}")
            return

