##Manage Workbook with C++
Learn how to Manage Workbook through the Aspose.Cells for C++ APIs.
Aspose.Cells for C++ provides a powerful and flexible API for managing workbooks and worksheets. This section explains how to create, open, and manipulate workbooks and worksheets programmatically.
## **Creating a New Workbook**
To create a new workbook:
1. Create an instance of the [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class.
2. Add worksheets to the workbook using the [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) class.
3. Save the workbook using the [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) method.
```cpp
#include <Aspose.Cells.h>
int main() {
Aspose::Cells::Startup();
// Create a new workbook
Aspose::Cells::Workbook workbook;
// Add a worksheet to the workbook
workbook.GetWorksheets().Add();
// Save the workbook
workbook.Save("output.xlsx");
Aspose::Cells::Cleanup();
return 0;
}
```
## **Opening an Existing Workbook**
To open an existing workbook:
1. Create an instance of the [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class and pass the file path to the constructor.
2. Access the worksheets using the [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) class.
3. Modify the workbook as needed.
4. Save the workbook using the [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) method.
```cpp
#include <Aspose.Cells.h>
int main() {
Aspose::Cells::Startup();
Aspose::Cells::Workbook workbook("input.xlsx");
auto worksheet = workbook.GetWorksheets().Get(0);
worksheet.GetCells().Get(0, 0).SetValue("Hello, World!");
workbook.Save("output.xlsx");
Aspose::Cells::Cleanup();
return 0;
}
```
## **Managing Worksheets**
Aspose.Cells for C++ provides a wide range of methods for managing worksheets, including adding, removing, and renaming worksheets.
### **Adding a Worksheet**
To add a new worksheet:
1. Access the [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) class from the workbook.
2. Use the [Add](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/add/) method to add a new worksheet.
```cpp
#include <Aspose.Cells.h>
int main() {
Aspose::Cells::Startup();
// Create a new workbook
Aspose::Cells::Workbook workbook;
// Add a new worksheet
workbook.GetWorksheets().Add("NewSheet");
// Save the workbook
workbook.Save("output.xlsx");
Aspose::Cells::Cleanup();
return 0;
}
```
### **Removing a Worksheet**
To remove a worksheet:
1. Access the [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) class from the workbook.
2. Use the [RemoveAt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/removeat/) method to remove a worksheet by index.
```cpp
#include <Aspose.Cells.h>
int main() {
Aspose::Cells::Startup();
// Open an existing workbook
Aspose::Cells::Workbook workbook("input.xlsx");
// Remove the first worksheet
workbook.GetWorksheets().RemoveAt(0);
// Save the workbook
workbook.Save("output.xlsx");
Aspose::Cells::Cleanup();
return 0;
}
```
### **Renaming a Worksheet**
To rename a worksheet:
1. Access the [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class from the workbook.
2. Use the [SetName](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/setname/) method to rename the worksheet.
```cpp
#include <Aspose.Cells.h>
int main() {
Aspose::Cells::Startup();
Aspose::Cells::Workbook workbook("input.xlsx");
auto worksheet = workbook.GetWorksheets().Get(0);
worksheet.SetName("RenamedSheet");
workbook.Save("output.xlsx");
Aspose::Cells::Cleanup();
return 0;
}
```
## **Conclusion**
Aspose.Cells for C++ provides a comprehensive set of tools for managing workbooks and worksheets. Whether you need to create a new workbook, open an existing one, or manipulate worksheets, Aspose.Cells makes it easy to work with Excel files programmatically.
