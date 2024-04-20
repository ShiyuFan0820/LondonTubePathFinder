# Unit Test

The unit test results for each function or method in a unit test cannot affect the next test, but for this project, the results of some methods in a class influence each other. For example, in `LoadData.py`, the return values of all other methods in class `StationInfo` are related to the `LoadData` method. So when writing the unit test, the `LoadData` method should be invoked in the `setUp` method.
