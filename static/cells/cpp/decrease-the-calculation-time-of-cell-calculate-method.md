##Decrease the Calculation Time of Cell.Calculate method with C++
This article introduces how to use Aspose.Cells library to reduce the calculation time of cell calculation methods in Microsoft Excel. By loading an existing Excel file or creating a new one, we can use the methods provided by Aspose.Cells to optimize the cell calculation method and improve its performance. Finally, we save the modified Excel file to disk.
## **Possible Usage Scenarios**
Normally, we recommend users to call [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) method once and then get the calculated values of the individual cells. But sometimes, users do not want to calculate the entire workbook. They just want to calculate a single cell. Aspose.Cells provides [**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getrecursive/) property which you can set to **false** and it will decrease the calculation time of individual cells significantly. Because when the recursive property is set to **true**, then all the dependents of cells are recalculated on each call. But when the recursive property is **false**, then dependent cells are calculated only once and are not calculated again on subsequent calls.
## **Decrease the Calculation Time of Cell.Calculate() method**
The following sample code illustrates the usage of [**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getrecursive/) property. Please execute this code with the given [sample excel file](5113710.xlsx) and check its console output. You will find that setting the recursive property to **false** has decreased the calculation time significantly. Please also read the comments for a better understanding of this property.
```c++
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
void TestCalcTimeRecursive(bool isRecursive) {
Workbook* workbook = new Workbook();
CalculationOptions options;
options.SetRecursive(isRecursive);
auto start = std::chrono::high_resolution_clock::now();
workbook->CalculateFormula(&options);
auto end = std::chrono::high_resolution_clock::now();
auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();
std::cout << "Time (recursive=" << isRecursive << "): " << duration << " ms" << std::endl;
delete workbook;
}
int main() {
Aspose::Cells::Startup();
TestCalcTimeRecursive(true);
TestCalcTimeRecursive(false);
Aspose::Cells::Cleanup();
return 0;
}
```
```cpp
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace std::chrono;
void TestCalcTimeRecursive(bool rec) {
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
Workbook wb(srcDir + u"sample.xlsx");
Worksheet ws = wb.GetWorksheets().Get(0);
CalculationOptions opts;
opts.SetRecursive(rec);
auto start = high_resolution_clock::now();
for (int i = 0; i < 1000000; i++) {
ws.GetCells().Get(u"A1").Calculate(opts);
}
auto stop = high_resolution_clock::now();
auto duration = duration_cast<milliseconds>(stop - start);
long estimatedTime = duration.count() / 1000;
std::cout << "Recursive " << rec << ": " << estimatedTime << " seconds" << std::endl;
}
int main() {
Aspose::Cells::Startup();
TestCalcTimeRecursive(true);
TestCalcTimeRecursive(false);
Aspose::Cells::Cleanup();
return 0;
}
```
## **Console Output**
This is the console output of the above sample code when executed with the given [sample excel file](5113710.xlsx) on our machine. Please note, your output may differ but the elapsed time after setting the recursive property to **false** will always be less than setting it to **true**.
Recursive True: 96 seconds
Recursive False: 42 seconds
