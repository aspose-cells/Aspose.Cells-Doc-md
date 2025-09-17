##Custom Validation in GridWeb
This article introduce custom validation in GridWeb .
## **Possible Usage Scenarios**
Aspose.Cells.GridWeb provide kinds of validation than normal defined in cells validation api.
the normal validation type in cells :<https://docs.aspose.com/cells/net/data-validation/>
the normal validation usage in GridWeb demo: <https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples_GridWeb/GridWeb.Net4/CSharp/Miscellaneous/Common/DataValidation.aspx.cs>
here we can check GridValidationType: <https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridvalidationtype/>
below is the extended validation which we can use in GridWeb
## **GridValidationType.DropDownList**
code:
```C#
// ExStart:AddDropDownListValidation
// Accessing the cells collection of the worksheet that is currently active
GridWorksheet sheet = GridWeb1.WorkSheets[GridWeb1.ActiveSheetIndex];
// Access "B1" cell and add some text
GridCell cell = sheet.Cells[0, 1];
cell.PutValue("Select Degree:");
// Accessing "C1" cell
cell = sheet.Cells[0, 2];
// Creating DropDownList validation for the "C1" cell
var validation = cell.CreateValidation(GridValidationType.DropDownList, true);
// Adding values to DropDownList validation
var values = new System.Collections.Specialized.StringCollection();
values.Add("Bachelor");
values.Add("Master");
values.Add("Doctor");
validation.ValueList = values;
```
result:
![todo:the validation result](gridvalidation_dropdownlist.png)
## **GridValidationType.FreeList**
code:
```C#
GridValidation validationOfList = this.GridWeb1.ActiveSheet.Validations.Add("c1");
validationOfList.ValidationType = GridValidationType.DropDownList;
StringCollection  C10List = new StringCollection();
C10List.Add("Fortran");
C10List.Add("Pascal");
C10List.Add("C++");
C10List.Add("Visual Basic");
C10List.Add("Java");
C10List.Add("C#");
validationOfList.ValueList = C10List;
```
result:
![todo:the validation result](gridvalidation_freelist.png)
## **GridValidationType.CustomExpression**
code:
```C#
var sheet = GridWeb1.ActiveSheet;
GridCell cell = sheet.Cells["B1"];
cell.PutValue("Please enter Date in cell C3 e.g. 2018-02-18");
//Access cell B3 and add the Date Pattern
cell = sheet.Cells["B3"];
cell.PutValue("Date (yyyy-mm-dd):");
// Access cell C3 and add to it custom expression validation to accept dates in yyyy-mm-dd format
cell = sheet.Cells["C3"];
var validation = cell.CreateValidation(GridValidationType.CustomExpression, true);
validation.RegEx = @"\d{4}-\d{2}-\d{2}";
//Set the column widths
sheet.Cells.SetColumnWidth(1, 40);
sheet.Cells.SetColumnWidth(2, 30);
//Set style number
sheet.Cells["C3"].SetNumberType((int)NumberType.EasternDate5);
// Assigning the name of JavaScript function to OnCellErrorClientFunction property of GridWeb
GridWeb1.OnCellErrorClientFunction = "ValidationErrorFunction";
```
add javascript function in client page
```javascript
function ValidationErrorFunction()
{
// Showing an alert message where "this" refers to GridWeb
console.log(this.id + ": Please correct your input error.");
}
```
result:
after enter invalid value
![todo:the validation result](gridvalidation_customexpression.png)
## **GridValidationType.Boolean**
code:
```C#
//add boolean validation at d1
GridWeb1.ActiveSheet.Cells[0, 3].CreateValidation(GridValidationType.Boolean,true);
```
result:
after enter invalid value
![todo:the validation result](gridvalidation_bool.png)
after enter true value
![todo:the validation result](gridvalidation_bool2.png)
## **GridValidationType.DateTime**
code:
```C#
//add DateTime validation at d3
GridWeb1.ActiveSheet.Cells[2, 3].CreateValidation(GridValidationType.DateTime, true);
```
result:
![todo:the validation result](gridvalidation_datetime.png)
## **GridValidationType.CheckBox**
code:
```C#
//add checkbox validation at d1
GridWeb1.ActiveSheet.Cells[0, 3].CreateValidation(GridValidationType.CheckBox,true);
```
result:
![todo:the validation result](gridvalidation_checkbox.png)
## **GridValidationType.CustomFunction**
code:
```C#
//add boolean validation at d4
GridValidation customValidation= GridWeb1.ActiveSheet.Cells[3, 3].CreateValidation(GridValidationType.CustomFunction, true);
customValidation.ClientValidationFunction = "MyClientValidation";
```
add javascript function in client page
```javascript
function MyClientValidation(source, value)
{
if (Number(value) > 10000)
return true;
else
return false;
}
```
result: after enter invalid value at d4
![todo:the validation result](gridvalidation_customfunction.png)
## **GridValidationType.CustomServerFunction**
code:
```C#
//define server side validation class which implment GridCustomServerValidation and ISerializable
// GridCustomServerValidation and ISerializable are the required interface to be done
class myservervalid : GridCustomServerValidation, ISerializable
{
string s;
void ISerializable.GetObjectData(System.Runtime.Serialization.SerializationInfo info, System.Runtime.Serialization.StreamingContext context)
{
info.AddValue("s",s);
}
protected myservervalid(SerializationInfo info, StreamingContext context)
{
s= info.GetString("s");
}
public myservervalid()
{
}
public string Validate(GridWorksheet sheet, int row, int col, string value)
{
if (row % 2 == 1)
{
return "not passed";
}
else
{
return "";
}
}
}
//add CustomServerFunction validation at G5 to G8
GridValidation val = this.GridWeb1.ActiveSheet.Validations.Add(new GridCellArea(5,6, 8, 6));
val.ValidationType = GridValidationType.CustomServerFunction;
val.ServerValidation = new myservervalid();
val.ClientValidationFunction=("ValidationErrorClientFunctionCallback");
val.ErrorMessage=("error message is here");
val.ErrorTitle=("this is error title");
```
add javascript function in client page
```javascript
var lastselectvalue = null;
var localvalue = {};
function ValidationErrorClientFunctionCallback(cell,msg)
{
//Get the error message string.
var errmsg1 = getattr(cell, "errmsg");
//Show the error message in the client dialog.
console.log(errmsg1);
//Showing an alert message where "this" refers to GridWeb
alert(this.id + "----> " + msg + " Previous value will be restored.");
$("#errmsg").text(msg);
console.log("Selected cell:" + " row:" + this.getCellRow(cell) + ",col:" + this.getCellColumn(cell));
//Get the GridWeb.
var who = this;
//Restore to valid value/previous value.
who.setValid(cell);
var key = this.acttab + "_" + this.getCellRow(cell) + "_" + this.getCellColumn(cell);
lastselectvalue = localvalue[key];
setInnerText(cell.children[0], lastselectvalue);
}
```
result: after enter value at g6
![todo:the validation result](gridvalidation_customserverfunction.png)
