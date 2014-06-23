import lldb
import lldb.formatters.Logger
import summaries
import synthetics

SyntheticDylanValue = synthetics.SyntheticDylanValue
dylan_byte_string_summary = summaries.dylan_byte_string_summary
dylan_object_summary = summaries.dylan_object_summary
dylan_simple_object_vector_summary = summaries.dylan_simple_object_vector_summary
dylan_symbol_summary = summaries.dylan_symbol_summary
dylan_value_summary = summaries.dylan_value_summary

def __lldb_init_module(debugger, internal_dict):
  debugger.HandleCommand('type format    add dylan_value -f hex')
  debugger.HandleCommand('type synthetic add dylan_value -l dylan.SyntheticDylanValue -w dylan')
  debugger.HandleCommand('type summary   add dylan_byte_string -F dylan.dylan_byte_string_summary -w dylan')
  debugger.HandleCommand('type summary   add dylan_object -F dylan.dylan_object_summary -w dylan')
  debugger.HandleCommand('type summary   add dylan_simple_object_vector -F dylan.dylan_simple_object_vector_summary -w dylan')
  debugger.HandleCommand('type summary   add dylan_symbol -F dylan.dylan_symbol_summary -w dylan')
  debugger.HandleCommand('type summary   add dylan_value -F dylan.dylan_value_summary -e -w dylan')
  debugger.HandleCommand('type category enable dylan')
