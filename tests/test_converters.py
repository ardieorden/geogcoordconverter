import pytest
from geogcoordconverter.converter import convert_dd_to_dms

@pytest.mark.parametrize("dd", [(77.0089, (77, 0, 32))])
def test_convert_dd_to_dms_value(dd):
	"""
	Test if convert_dd_to_dms value returns the expected value
	"""

	dd_input, expected_return = dd
	dms_answer = convert_dd_to_dms(dd_input)

	assert dms_answer == expected_return
