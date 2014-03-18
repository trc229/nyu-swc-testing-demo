#!/usr/bin/env python

"""This is the nosetest module for the coordinates2Region.py"""

from coordinates2Region import coordinates2Region

def test_coordinates2Region():
	"""This function tests the functionality for the coordinates2Region function."""

	#Edges
	assert coordinates2Region({'x':1, 'y':1}) == [1], 'Something failed.'
	assert coordinates2Region({'x':1, 'y':350}) == [2], 'Something failed.'
	assert coordinates2Region({'x':350, 'y':350}) == [3], 'Something failed.'
	assert coordinates2Region({'x':350, 'y':1}) == [4], 'Something failed.'

	#Inner Boundaries

	#Outter Boundaries

	#Invalid Tests


