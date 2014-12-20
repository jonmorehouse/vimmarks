import test_setup
import mock
import vim

import config

def test_to_vim_varname():
    assert config.to_vim_varname("name") == "Name"
    assert config.to_vim_varname("name_name_name") == "NameNameName"


@mock.patch('vim.eval', return_value= "vim_name")
def test_config(eval_mock):
    value = config.name

    eval_mock.assert_called_with_once("g:%sName" % config.variable_namespace)
    assert value == eval_mock.return_value

@mock.patch('vim.eval', return_value= "55")
def test_int_config(vim_mock):
    value = config.number_int
    assert value == 55


