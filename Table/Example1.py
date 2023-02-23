from dash import Dash, dash_table
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

app = Dash(__name__)

app.layout = dash_table.DataTable(
    df.to_dict('records'), 
    [{"name": i, "id": i} for i in df.columns]
    )

if __name__ == '__main__':
    app.run_server(debug=True)

"""
Allowed arguments: active_cell, cell_selectable, column_selectable, columns, css, data, 
data_previous, data_timestamp, derived_filter_query_structure, derived_viewport_data, 
derived_viewport_indices, derived_viewport_row_ids, 
derived_viewport_selected_columns, derived_viewport_selected_row_ids, 
derived_viewport_selected_rows, derived_virtual_data, derived_virtual_indices, 
derived_virtual_row_ids, derived_virtual_selected_row_ids, derived_virtual_selected_rows, 
dropdown, dropdown_conditional, dropdown_data, editable, end_cell, export_columns, 
export_format, export_headers, fill_width, filter_action, filter_options, filter_query, 
fixed_columns, fixed_rows, hidden_columns, id, include_headers_on_copy_paste, is_focused, 
loading_state, locale_format, markdown_options, merge_duplicate_headers, page_action, 
page_count, page_current, page_size, persisted_props, persistence, persistence_type, 
row_deletable, row_selectable, selected_cells, selected_columns, selected_row_ids, 
selected_rows, sort_action, sort_as_null, sort_by, sort_mode, start_cell, style_as_list_view,
style_cell, style_cell_conditional, style_data, style_data_conditional, style_filter, 
style_filter_conditional, style_header, style_header_conditional, style_table, tooltip, 
tooltip_conditional, tooltip_data, tooltip_delay, tooltip_duration, tooltip_header, 
virtualization
"""