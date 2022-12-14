---
title: Público API Cambios en Aspose.Cells 16.12.0
type: docs
weight: 10
url: /es/cpp/public-api-changes-in-aspose-cells-16-12-0/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 16.11.0 a la 16.12.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Soporte para tablas dinámicas**
La segunda versión de Aspose.Cells para C++ admite la creación y la manipulación de tablas dinámicas. Aspose.Cells para C++ proporciona la clase IPivotTable que representa un objeto de tabla dinámica, mientras que IPivotTableCollection representa una colección de tablas dinámicas. Se puede acceder a IPivotTableCollection a través del objeto IWorksheet y se puede agregar una nueva tabla dinámica a la colección mientras se usa el método IPivotTableCollection.Add.

 El siguiente fragmento de código demuestra lo simple que es usar Aspose.Cells para C++ API para[crear tablas dinámicas desde cero](/cells/es/cpp/create-pivot-table/).

**C++**

{{< highlight "csharp" >}}

 //Load the sample excel file

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook();

//Access first worksheet

intrusive_ptr<IWorksheet> ws = wb->GetIWorksheets()->GetObjectByIndex(0);

//Add source data for pivot table

intrusive_ptr<String> str = new String("Fruit");

ws->GetICells()->GetObjectByIndex(new String("A1"))->PutValue(str);

str = new String("Quantity");

ws->GetICells()->GetObjectByIndex(new String("B1"))->PutValue(str);

str = new String("Price");

ws->GetICells()->GetObjectByIndex(new String("C1"))->PutValue(str);

str = new String("Apple");

ws->GetICells()->GetObjectByIndex(new String("A2"))->PutValue(str);

str = new String("Orange");

ws->GetICells()->GetObjectByIndex(new String("A3"))->PutValue(str);

ws->GetICells()->GetObjectByIndex(new String("B2"))->PutValue(3);

ws->GetICells()->GetObjectByIndex(new String("B3"))->PutValue(4);

ws->GetICells()->GetObjectByIndex(new String("C2"))->PutValue(2);

ws->GetICells()->GetObjectByIndex(new String("C3"))->PutValue(1);

//Add pivot table

int idx = ws->GetIPivotTables()->Add(new String("A1:C3"), new String("E5"), new String("MyPivotTable"));

//Access created pivot table

intrusive_ptr<IPivotTable> pt = ws->GetIPivotTables()->GetObjectByIndex(idx);

//Manipulate pivot table rows, columns and data fields

pt->AddFieldToArea(PivotFieldType_Row, pt->GetIBaseFields()->GetObjectByIndex(0));

pt->AddFieldToArea(PivotFieldType_Data, pt->GetIBaseFields()->GetObjectByIndex(1));

pt->AddFieldToArea(PivotFieldType_Data, pt->GetIBaseFields()->GetObjectByIndex(2));

pt->AddFieldToArea(PivotFieldType_Column, pt->GetIDataField());

//Set pivot table style

pt->SetPivotTableStyleType(PivotTableStyleType_PivotTableStyleMedium9);

//Save the output excel file

wb->Save(outputPath);

{{< /highlight >}}

Además de crear nuevas tablas dinámicas, las API Aspose.Cells para C++ también admiten la manipulación de tablas dinámicas existentes. El API actualmente admite cambiar los datos en el rango de origen de la tabla dinámica y luego actualizarlos. Una vez que la tabla dinámica se haya manipulado como se desea, es mejor usar los métodos IPivotTable.RefreshData e IPivotTable.CalculateData para actualizar la tabla dinámica con el origen de datos actualizado.

 El siguiente fragmento de código usa Aspose.Cells para C++ API para[manipular una tabla dinámica existente](/cells/es/cpp/manipulate-pivot-table/).

**C++**

{{< highlight "csharp" >}}

 //Load the sample excel file

intrusive_ptr wb = Factory::CreateIWorkbook(samplePath);

//Access first worksheet

intrusive_ptr ws = wb->GetIWorksheets()->GetObjectByIndex(0);

//Change value of cell B3 which is inside the source data of pivot table

intrusive_ptr str = new String("Cup");

ws->GetICells()->GetObjectByIndex(new String("B3"))->PutValue(str);

//Get the value of cell H8 before refreshing pivot table

intrusive_ptr val = ws->GetICells()->GetObjectByIndex(new String("H8"))->GetStringValue();

printf("Before refreshing Pivot Table value of cell H8: %s\r\n%", val->charValue());

//Access pivot table, refresh and calculate it

intrusive_ptr pt = ws->GetIPivotTables()->GetObjectByIndex(0);

pt->RefreshData();

pt->CalculateData();

//Get the value of cell H8 after refreshing pivot table

val = ws->GetICells()->GetObjectByIndex(new String("H8"))->GetStringValue();

printf("After refreshing Pivot Table value of cell H8: %s\r\n%", val->charValue());

//Save the output excel file

wb->Save(outputPath);

{{< /highlight >}}
### **Compatibilidad con reglas de formato condicional**
 Aspose.Cells para C++ ahora brinda la capacidad de agregar reglas de formato condicional a la hoja de trabajo al exponer la clase IFormatCondition. La clase antes mencionada proporciona además los siguientes métodos para[aplicar las reglas de formato condicional](/cells/es/cpp/apply-conditional-formatting-in-worksheet/) según los requisitos de la aplicación.

- IFormatCondition.GetIAboveAverage
- IFormatCondition.GetIColorScale
- IFormatCondition.GetIDataBar
- IFormatCondition.GetIIconSet
- IFormatCondition.GetITop10

El siguiente código de ejemplo muestra cómo agregar una regla de formato condicional de tipo Cell Valor en las celdas A1 y B2.

**C++**

{{< highlight "csharp" >}}

 //Create an empty workbook

intrusive_ptr wb = Factory::CreateIWorkbook();

//Access first worksheet

intrusive_ptr ws = wb->GetIWorksheets()->GetObjectByIndex(0);

//Adds an empty conditional formatting

int idx = ws->GetIConditionalFormattings()->Add();

intrusive_ptr fcs = ws->GetIConditionalFormattings()->GetObjectByIndex(idx);

//Set the conditional format range

intrusive_ptr ca = ICellArea::CreateICellArea(new String("A1"), new String("A1"));

fcs->AddArea(ca);

ca = ICellArea::CreateICellArea(new String("B2"), new String("B2"));

fcs->AddArea(ca);

//Add condition and set the background color

idx = fcs->AddCondition(FormatConditionType_CellValue, OperatorType_Between, new String("=A2"), new String("100"));

intrusive_ptr fc = fcs->GetObjectByIndex(idx);

fc->GetIStyle()->SetBackgroundColor(Color::GetRed());

//User friendly message to test the output excel file.

StringPtr msgStr = new String("Red color in cells A1 and B2 is because of Conditional Formatting.");

ws->GetICells()->GetObjectByIndex(new String("A10"))->PutValue(msgStr);

//Save the output excel file

wb->Save(outputPath);

{{< /highlight >}}
### **Soporte para hipervínculos**
 Aspose.Cells para C++ ahora es compatible[agregar hipervínculos a las celdas de la hoja de trabajo](/cells/es/cpp/add-hyperlinks-to-the-cells/). Para proporcionar esta característica, el Aspose.Cells para C++ 16.12.0 ha expuesto la clase IHyperlinkCollection a la que se puede acceder a través del objeto IWorksheet, mientras que se puede agregar un hipervínculo a la colección al usar el método IHyperlinkCollection.Add como se muestra a continuación.

**C++**

{{< highlight "csharp" >}}

 //Create a new workbook

intrusive_ptr wb = Factory::CreateIWorkbook();

//Get the first worksheet

intrusive_ptr wsc = wb->GetIWorksheets();

intrusive_ptr ws = wsc->GetObjectByIndex(0);

//Add hyperlink in cell C7 and make use of its various methods

intrusive_ptr hypLnks = ws->GetIHyperlinks();

int idx = hypLnks->Add(new String("C7"), 1, 1, new String("http://www.aspose.com/"));

intrusive_ptr lnk = hypLnks->GetObjectByIndex(idx);

lnk->SetTextToDisplay(new String("Aspose"));

lnk->SetScreenTip(new String("Link to Aspose Website"));

//Save the workbook in xlsx format

wb->Save(dirPath->Append(new String("output.xlsx")), SaveFormat_Xlsx);

{{< /highlight >}}
### **Compatibilidad con propiedades de documentos**
La aplicación de Excel admite 2 tipos de propiedades de documentos que se enumeran a continuación.

- Propiedades definidas por el sistema (integradas): las propiedades integradas contienen información general sobre el documento, como el título del documento, el nombre del autor, las estadísticas del documento, etc.
- Propiedades definidas por el usuario (personalizadas): propiedades personalizadas definidas por el usuario final en forma de par de nombre y valor.

Aspose.Cells para soportes C++[administrar ambos tipos de propiedades de documentos, integradas y personalizadas](/cells/es/cpp/managing-document-properties/). Aspose.Cells' La clase IWorkbook representa un archivo de Excel. Para acceder a las propiedades del documento integrado, utilice IWorkbook.GetBuiltInDocumentProperties mientras que se puede acceder a las propiedades del documento personalizado utilizando el método IWorkbook.GetCustomDocumentProperties.

El siguiente código de muestra carga una hoja de cálculo de muestra existente y lee las propiedades integradas del documento, como Título, Asunto y propiedad personalizada con el nombre MyCustom1.

**C++**

{{< highlight "csharp" >}}

 //Load the sample excel file

intrusive_ptr wb = Factory::CreateIWorkbook(samplePath);

//Read built-in title and subject properties

StringPtr strTitle = wb->GetIBuiltInDocumentProperties()->GetTitle();

StringPtr strSubject = wb->GetIBuiltInDocumentProperties()->GetSubject();

printf("Title: %s\r\n", strTitle->charValue());

printf("Subject: %s\r\n", strSubject->charValue());

printf("\r\n");

//Modify built-in title and subject properties

strTitle = new String("Aspose.Cells New Title");

strSubject = new String("Aspose.Cells New Subject");

wb->GetIBuiltInDocumentProperties()->SetTitle(strTitle);

wb->GetIBuiltInDocumentProperties()->SetSubject(strSubject);

//Read the custom property

StringPtr strCustomPropName = new String("MyCustom1");

StringPtr strCustomPropValue = wb->GetICustomDocumentProperties()->GetObjectByIndex(strCustomPropName)->ToString();

printf("MyCustom1: %s\r\n", strCustomPropValue->charValue());

//Add a new custom property

strCustomPropName = new String("MyCustom5");

strCustomPropValue = new String("This is my custom five.");

wb->GetICustomDocumentProperties()->AddIDocumentProperty(strCustomPropName, strCustomPropValue);

//Save the output excel file

wb->Save(outputPath);

{{< /highlight >}}
### **Soporte para ListObjects**
 Una tabla de Excel es una matriz de celdas que contiene cualquier cantidad de filas y columnas, mientras que la misma tabla se denomina Objeto de lista en Aspose.Cells para las API C++. El espacio de nombres Aspose::Cells::Tables contiene todas las clases necesarias que se ocupan de las operaciones relacionadas con los objetos de la lista. Las clases más dignas de mención son IListObject e IListObjectCollection que permiten[crear y formatear objetos de lista](/cells/es/cpp/create-and-format-table/) y así.

El siguiente código de muestra carga el archivo de hoja de cálculo de muestra y luego crea un objeto de lista (tabla) en un rango A1: H10, luego utiliza sus diversos métodos para mostrar el subtotal.

**C++**

{{< highlight "csharp" >}}

 //Load the sample excel file

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook(samplePath);

//Access first worksheet

intrusive_ptr<IWorksheet> ws = wb->GetIWorksheets()->GetObjectByIndex(0);

//Add table i.e. list object

int idx = ws->GetIListObjects()->Add(new String("A1"), new String("H10"), true);

//Access the newly added list object

intrusive_ptr<IListObject> lo = ws->GetIListObjects()->GetObjectByIndex(idx);

//Make use of its display methods

lo->SetShowHeaderRow(true);

lo->SetShowTableStyleColumnStripes(true);

lo->SetShowTotals(true);

//Set its style

lo->SetTableStyleType(TableStyleType_TableStyleLight12);

//Set total functions of 3rd, 4th and 5th columns

lo->GetIListColumns()->GetObjectByIndex(2)->SetTotalsCalculation(TotalsCalculation_Min);

lo->GetIListColumns()->GetObjectByIndex(3)->SetTotalsCalculation(TotalsCalculation_Max);

lo->GetIListColumns()->GetObjectByIndex(4)->SetTotalsCalculation(TotalsCalculation_Count);

//Save the output excel file

wb->Save(outputPath);

{{< /highlight >}}
### **Compatibilidad con la agrupación de filas y columnas**
 Aspose.Cells para C++ API se puede usar para agrupar filas y columnas mientras se usa la clase ICells, que es básicamente la colección de todas las celdas en una hoja de cálculo determinada. La clase ICells ofrece los métodos GroupRows y GroupColumns para[agrupar filas y columnas](/cells/es/cpp/group-rows-and-columns-of-worksheet/) respectivamente.

El siguiente fragmento de código demuestra el escenario de uso simple de los dos métodos mencionados anteriormente.

**C++**

{{< highlight "csharp" >}}

 //Create an empty workbook

intrusive_ptr wb = Factory::CreateIWorkbook();

//Add worksheet for grouping rows

intrusive_ptr grpRows = wb->GetIWorksheets()->GetObjectByIndex(0);

grpRows->SetName(new String("GroupRows"));

//Add worksheet for grouping columns

int idx = wb->GetIWorksheets()->Add();

intrusive_ptr grpCols = wb->GetIWorksheets()->GetObjectByIndex(idx);

grpCols->SetName(new String("GroupColumns"));

//Add sample values in both worksheets

for (int i = 0; i<50; i++)

{

	intrusive_ptr str = new String("Text");

	grpRows->GetICells()->GetObjectByIndex(i, 0)->PutValue(str);

	grpCols->GetICells()->GetObjectByIndex(0, i)->PutValue(str);

}

//Grouping rows at first level

grpRows->GetICells()->GroupRows(0, 10);

grpRows->GetICells()->GroupRows(12, 22);

grpRows->GetICells()->GroupRows(24, 34);

//Grouping rows at second level

grpRows->GetICells()->GroupRows(2, 8);

grpRows->GetICells()->GroupRows(14, 20);

grpRows->GetICells()->GroupRows(28, 30);

//Grouping rows at third level

grpRows->GetICells()->GroupRows(5, 7);

//Grouping columns at first level

grpCols->GetICells()->GroupColumns(0, 10);

grpCols->GetICells()->GroupColumns(12, 22);

grpCols->GetICells()->GroupColumns(24, 34);

//Grouping columns at second level

grpCols->GetICells()->GroupColumns(2, 8);

grpCols->GetICells()->GroupColumns(14, 20);

grpCols->GetICells()->GroupColumns(28, 30);

//Grouping columns at third level

grpCols->GetICells()->GroupColumns(5, 7);

//Save the output excel file

wb->Save(outputPath);

{{< /highlight >}}
### **Soporte para temas**
Aspose.Cells para C++ Las API ahora admiten el uso y la manipulación de los temas que ofrece la aplicación Excel.
#### **Capacidad para aplicar los colores del tema personalizado**
 El siguiente fragmento intenta[crear un nuevo tema con colores personalizados](/cells/es/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/) para el libro de trabajo.

**C++**

{{< highlight "csharp" >}}

 //Create a workbook

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook();

//Create array of custom theme colors

intrusive_ptr<Array1D<Color*>> clrs = new Array1D<Color*>(12);

//Background1

clrs->SetValue(Color::GetRed(), 0);

//Text1

clrs->SetValue(Color::GetRed(), 1);

//Background2

clrs->SetValue(Color::GetRed(), 2);

//Text2

clrs->SetValue(Color::GetRed(), 3);

//Accent1

clrs->SetValue(Color::GetRed(), 4);

//Accent2

clrs->SetValue(Color::GetGreen(), 5);

//Accent3

clrs->SetValue(Color::GetGreen(), 6);

//Accent4

clrs->SetValue(Color::GetGreen(), 7);

//Accent5

clrs->SetValue(Color::GetGreen(), 8);

//Accent6

clrs->SetValue(Color::GetBlue(), 9);

//Hyperlink

clrs->SetValue(Color::GetBlue(), 10);

//Followed Hyperlink

clrs->SetValue(Color::GetBlue(), 11);

//Apply custom theme colors on workbook

wb->CustomTheme(new String("AnyTheme"), clrs);

//Save the workbook

wb->Save(outputPath);

{{< /highlight >}}
#### **Compatibilidad con la manipulación de los colores del tema**
El siguiente código de ejemplo muestra cómo[leer y modificar los colores del tema del libro de trabajo](/cells/es/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/). El código de muestra carga una hoja de cálculo existente, lee los colores de su tema, es decir, Accent1-Accent6, y modifica los colores antes de guardar la hoja de cálculo.

**C++**

{{< highlight "csharp" >}}

 //Load the sample excel file

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook(samplePath);

//Read these theme colors i.e. Accent1 till Accent6

intrusive_ptr<Color> clr_Accent1 = wb->GetThemeColor(ThemeColorType_Accent1);

intrusive_ptr<Color> clr_Accent2 = wb->GetThemeColor(ThemeColorType_Accent2);

intrusive_ptr<Color> clr_Accent3 = wb->GetThemeColor(ThemeColorType_Accent3);

intrusive_ptr<Color> clr_Accent4 = wb->GetThemeColor(ThemeColorType_Accent4);

intrusive_ptr<Color> clr_Accent5 = wb->GetThemeColor(ThemeColorType_Accent5);

intrusive_ptr<Color> clr_Accent6 = wb->GetThemeColor(ThemeColorType_Accent6);

//Print all of them. ffff00 means Yellow

printf("Accent1: %x\r\n", clr_Accent1->ToArgb());

printf("Accent2: %x\r\n", clr_Accent2->ToArgb());

printf("Accent3: %x\r\n", clr_Accent3->ToArgb());

printf("Accent4: %x\r\n", clr_Accent4->ToArgb());

printf("Accent5: %x\r\n", clr_Accent5->ToArgb());

printf("Accent6: %x\r\n", clr_Accent6->ToArgb());

//Set all of them to Red

wb->SetThemeColor(ThemeColorType_Accent1, Color::GetRed());

wb->SetThemeColor(ThemeColorType_Accent2, Color::GetRed());

wb->SetThemeColor(ThemeColorType_Accent3, Color::GetRed());

wb->SetThemeColor(ThemeColorType_Accent4, Color::GetRed());

wb->SetThemeColor(ThemeColorType_Accent5, Color::GetRed());

wb->SetThemeColor(ThemeColorType_Accent6, Color::GetRed());

//Reading one of them after modifying, it will be ff0000 which means Red

printf("\r\nReading one of them after modifying, it will be ff0000 which means Red\r\n\r\n");

clr_Accent6 = wb->GetThemeColor(ThemeColorType_Accent6);

printf("Accent6: %x\r\n", (clr_Accent6->ToArgb())&0xffffff);

//Save the output excel file

wb->Save(outputPath);

{{< /highlight >}}
#### **Capacidad para copiar temas entre libros de trabajo**
El siguiente código de ejemplo muestra cómo[copiar tema de un libro de trabajo a otro](/cells/es/cpp/copy-theme-from-one-workbook-to-another/), que podría ser útil para aplicar temas integrados o personalizados en varias hojas de cálculo.

**C++**

{{< highlight "csharp" >}}

 //Read excel file that has Damask theme applied on it

intrusive_ptr<IWorkbook> damask = Factory::CreateIWorkbook(damaskPath);

//Read your sample excel file

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook(samplePath);

//Copy theme from source file

wb->CopyTheme(damask);

//Save the workbook in xlsx format

wb->Save(outputPath, SaveFormat_Xlsx);

{{< /highlight >}}
## **API renombradas**
Con el lanzamiento de Aspose.Cells para C++ 16.12.0, hemos cambiado el nombre de algunos métodos para mantener las interfaces unificadas. La lista de todas las API renombradas es la siguiente.
#### **Se cambió el nombre del método ICell::SetStyle a ICell::SetIStyle**
#### **Se cambió el nombre del método ICell::SetCharacters a ICell::SetIFontSettings**
#### **Se cambió el nombre del método ICellsColor::SetThemeColor a ICellsColor::SetIThemeColor**
#### **Se cambió el nombre del método ICells::SetStyle a ICells::SetIStyle**
#### **Se cambió el nombre del método ICellsHelper::GetDPI_i a ICellsHelper::GetDPI**
#### **Se cambió el nombre del método ICellsHelper::SetDPI_i a ICellsHelper::SetDPI**
#### **Se cambió el nombre del método ICellsHelper::GetVersion_i a ICellsHelper::GetVersion**
#### **Se cambió el nombre del método ICellsHelper::IsProtectedByRMS_i a ICellsHelper::IsProtectedByRMS**
#### **Se cambió el nombre del método ICellsHelper::IsProtectedByRMS_i a ICellsHelper::IsProtectedByRMS**
#### **Se cambió el nombre del método ICellsHelper::CellNameToIndex_i a ICellsHelper::CellNameToIndex**
#### **Se cambió el nombre del método ICellsHelper::CellIndexToName_i a ICellsHelper::CellIndexToName**
#### **Se cambió el nombre del método ICellsHelper::ColumnIndexToName_i a ICellsHelper::ColumnIndexToName**
#### **Se cambió el nombre del método ICellsHelper::ColumnNameToIndex_i a ICellsHelper::ColumnNameToIndex**
#### **Se cambió el nombre del método ICellsHelper::RowIndexToName_i a ICellsHelper::RowIndexToName**
#### **Se cambió el nombre del método ICellsHelper::RowNameToIndex_i a ICellsHelper::RowNameToIndex**
#### **Se cambió el nombre del método ICellsHelper::ConvertR1C1FormulaToA1_i a ICellsHelper::ConvertR1C1FormulaToA1**
#### **Se cambió el nombre del método ICellsHelper::ConvertA1FormulaToR1C1_i a ICellsHelper::ConvertA1FormulaToR1C1**
#### **Se cambió el nombre del método ICellsHelper::GetDateTimeFromDouble_i a ICellsHelper::GetDateTimeFromDouble**
#### **Se cambió el nombre del método ICellsHelper::GetDoubleFromDateTime_i a ICellsHelper::GetDoubleFromDateTime**
#### **Se cambió el nombre del método ICellsHelper::DetectLoadFormat_i a ICellsHelper::DetectLoadFormat**
#### **Se cambió el nombre del método ICellsHelper::DetectFileFormat_i a ICellsHelper::DetectFileFormat**
#### **Se cambió el nombre del método ICellsHelper::GetFontDir_i a ICellsHelper::GetFontDir**
#### **Se cambió el nombre del método ICellsHelper::SetFontDir_i a ICellsHelper::SetFontDir**
#### **Se cambió el nombre del método ICellsHelper::GetFontDirs_i a ICellsHelper::GetFontDirs**
#### **Se cambió el nombre del método ICellsHelper::SetFontDirs_i a ICellsHelper::SetFontDirs**
#### **Se cambió el nombre del método ICellsHelper::GetFontFiles_i a ICellsHelper::GetFontFiles**
#### **Se cambió el nombre del método ICellsHelper::SetFontFiles_i a ICellsHelper::SetFontFiles**
#### **Se cambió el nombre del método ICellsHelper::GetStartupPath_i a ICellsHelper::GetStartupPath**
#### **Se cambió el nombre del método ICellsHelper::SetStartupPath_i a ICellsHelper::SetStartupPath**
#### **Se cambió el nombre del método ICellsHelper::GetAltStartPath_i a ICellsHelper::GetAltStartPath**
#### **Se cambió el nombre del método ICellsHelper::SetAltStartPath_i a ICellsHelper::SetAltStartPath**
#### **Se cambió el nombre del método ICellsHelper::GetLibraryPath_i a ICellsHelper::GetLibraryPath**
#### **Se cambió el nombre del método ICellsHelper::SetLibraryPath_i a ICellsHelper::SetLibraryPath**
#### **Se cambió el nombre del método ICellsHelper::GetUsedColors_i a ICellsHelper::GetUsedColors**
#### **Se cambió el nombre del método ICellsHelper::AddAddInFunction_i a ICellsHelper::AddAddInFunction**
#### **Se cambió el nombre del método ICellsHelper::MergeFiles_i a ICellsHelper::MergeFiles**
#### **Se cambió el nombre del método IColumnCollection::GetByIndex_i a IColumnCollection::GetIColumn**
#### **Se cambió el nombre del método IFileFormatUtil::DetectFileFormat_i a IFileFormatUtil::DetectFileFormat**
#### **Se cambió el nombre del método IFileFormatUtil::ExtensionToSaveFormat_i a IFileFormatUtil::ExtensionToSaveFormat**
#### **Se cambió el nombre del método IFileFormatUtil::IsTemplateFormat_i a IFileFormatUtil::IsTemplateFormat**
#### **Se cambió el nombre del método IFileFormatUtil::LoadFormatToExtension_i a IFileFormatUtil::LoadFormatToExtension**
#### **Se cambió el nombre del método IFileFormatUtil::LoadFormatToSaveFormat_i a IFileFormatUtil::LoadFormatToSaveFormat**
#### **Se cambió el nombre del método IFileFormatUtil::SaveFormatToExtension_i a IFileFormatUtil::SaveFormatToExtension**
#### **Se cambió el nombre del método IFileFormatUtil::SaveFormatToLoadFormat_i a IFileFormatUtil::SaveFormatToLoadFormat**
#### **Renombrado método IRange::SetStyle a IRange::SetIStyle**
#### **Se cambió el nombre del método IFindOptions::SetRange a IFindOptions::SetIRange**
#### **Se cambió el nombre del método ILoadOptions::SetLoadDataOptions a ILoadOptions::SetILoadDataOptions**
#### **Se cambió el nombre del método IWorkbook::SetSettings a IWorkbook::SetISettings**
#### **Se cambió el nombre del método IWorkbook::SetDefaultStyle a IWorkbook::SetDefaultIStyle**
