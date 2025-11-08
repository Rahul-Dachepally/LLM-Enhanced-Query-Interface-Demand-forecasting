from database.schema import create_schema_context

def build_sql_prompt(natural_query, schema):
    '''
    Build prompt for SQL generation
    '''
    schema_context = create_schema_context(schema)
    
    prompt = f"""You are an expert SQL query generator for an M5 forecasting inventory database.

{schema_context}

Important Rules:
1. ALWAYS include a LIMIT clause (max 1000 rows)
2. Only generate SELECT queries (no INSERT, UPDATE, DELETE, DROP, etc.)
3. For sales data, columns starting with 'd_' represent daily sales (d_1, d_2, ... d_1913)
4. Use the latest available 'd_' column for current sales analysis
5. Return ONLY the SQL query without any explanation, markdown, or code blocks
6. Do not include semicolons at the end
7. Use proper SQL syntax for SQLite

Natural Language Query: {natural_query}

Generate the SQL query:"""
    
    return prompt

def build_explanation_prompt(sql):
    '''
    Build prompt for SQL explanation
    '''
    prompt = f"""Explain this SQL query in one concise sentence:
{sql}

Explanation:"""
    
    return prompt