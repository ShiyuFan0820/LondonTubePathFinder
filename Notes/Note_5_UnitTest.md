# Unit Test

1. The unit test results for each function or method in a unit test cannot affect the next test, but for this project, the results of some methods in a class influence each other. For example, in `LoadData.py`, the return values of all other methods in class `StationInfo` are related to the `LoadData` method. So, when writing the unit test, the `LoadData` method should be invoked in the `setUp` method.
2. When testing the `DisplayPaths` method, I used `assertEqual` at first to compare the expected path with the result that the `DisplayPaths` method returns, but this method doesn't return anything and only does the print job, so the test failed. In this case, I want to capture the printed output and verify it's correct, so `mock` can be used in this case.

