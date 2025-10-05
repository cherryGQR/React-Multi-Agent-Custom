# def _search_db(query: str,  top_k: int=4):
#
#     data = {
#     "user":"",
#     "query":query,
#     "collection_name":"",
#     "retrive_filter":"",
#     "retrive_params":{
#         "sparse":{"topk":top_k},
#         "fulltext":{"topk":top_k},
#         "rerank":{"topk":top_k,"model_name":"rrf","rerank_params":{}}
#         },
#     "return_fea":["content"]
#     }
#
#     url = ""
#
#     response = requests.post(url, json=data, stream=True)
#     result_dict=json.loads(response.content)
#     print(result_dict['data'])
#     texts = []
#     for item in result_dict['data']:
#         data = item['content']
#         texts.append(data)
#     # 将所有 full_text 合并为一个字符串
#     combined_text = "\n\n".join(texts)
#     return combined_text
#
# def _search_db(query: str, db_name="", table_name="",  top_k: int=10):
#     payload={
#         "db_name": db_name,
#         "table_name": table_name,
#         "query": query,
#         "index_types":["all"],
#         "output_str":["fulltext"],
#         "search_method":"rrf",
#         "seach_param":{"dense":10,"sparse":10,"fulltext":10,"rerank":top_k},
#         "emb_models":{"dense":"bge_m3","sparse":"bge_m3","colbert":"bge_m3"}
#     }
#     headers = {"Content-Type": "application/json"}
#     response = requests.post("",
#                             data=json.dumps(payload),
#                             headers=headers)
#     result_dict=json.loads(response.content)
#     texts = []
#     for item in result_dict['data']:
#         data = item['data']['fulltext']
#         texts.append(data)
#     # 将所有 full_text 合并为一个字符串
#     combined_text = "\n\n".join(texts)
#     return combined_text



def QUERY_UNDERSTAND_PROMPT(description, parameters_definition):

    QUERY_UNDERSTAND = f"""
    ## Profile
    - **language**: 中文
    - **description**: 你是一个资深问题理解专家（Query UnderStand Agent），负责理解用户输入的问题，并对问题中得参数进行解析，以及问题得改写。

    ### 核心职责
    - **用户问题解析**：深入理解用户输入问题中，每个参数得含义。
    - **用户问题改写**：在不改变用户问题含义得情况下，结合问题中每个参数得含义对问题进行改写，得到一个逻辑连贯，更加完整得问题描述。

    ### 流程管理
    - 严格执行“用户问题解析 -> 用户问题改写”的两阶段流程。

    ### 工作流程
    1.  **对用户问题进行解析**：结合所有参数的定义，以及用户问题中每个参数的含义解释，对问题中得参数进行解析提取，输出各个参数对应得参数类型（XML格式）。
    2.  **对用户问题进行描述**：在不改变用户问题含义得情况下，结合用户问题中每个参数的含义，对问题进行改写，得到一个逻辑连贯，更加完整得问题描述（XML格式）。

    ### 输出格式规范
    你必须**严格**使用以下XML标签格式进行输出和通信：

    <QueryUnderStand>
        <query_parameter_type>
            "参数类型":"参数值"（例如：）
            ...
        </query_parameter_type>
        <query_description>
            问题描述内容（例如：...）
        </query_description>
    </QueryUnderStand>

    ### 初始化示例
    **用户输入**："..."
    **Query UnderStand Agent输出**：
    <QueryUnderStand>
        <query_parameter_type>
            
        </query_parameter_type>
        <query_description>
            问题描述内容（例如：in_progress, completed, requires_adjustment）
        </query_description>
    </QueryUnderStand>

    ## 参考信息
    - 用户输入问题的参考信息如下：
   {parameters_definition}

    # 当前任务
    用户问题：{description}
    """

    return QUERY_UNDERSTAND