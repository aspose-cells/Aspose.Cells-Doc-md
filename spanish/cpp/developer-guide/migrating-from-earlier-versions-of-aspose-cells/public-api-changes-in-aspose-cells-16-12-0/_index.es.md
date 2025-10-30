---
title: Cambios en la API pública en Aspose.Cells 16.12.0
type: docs
weight: 10
url: /es/cpp/public-api-changes-in-aspose-cells-16-12-0/
---

{{% alert color="primary" %}} 

Este documento describe los cambios realizados en la API de Aspose.Cells desde la versión 16.11.0 hasta la 16.12.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases añadidas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento interno en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Soporte para tablas dinámicas**
La segunda versión de Aspose.Cells for C++ admite la creación y manipulación de tablas dinámicas. Aspose.Cells for C++ proporciona la clase IPivotTable que representa un objeto de tabla dinámica, mientras que IPivotTableCollection representa una colección de tablas dinámicas. La IPivotTableCollection se puede acceder a través del objeto IWorksheet y se puede agregar una nueva tabla dinámica a la colección mientras se utiliza el método IPivotTableCollection.Add.

El siguiente fragmento de código demuestra lo simple que es usar la API Aspose.Cells for C++ para [crear tablas dinámicas desde cero](/cells/es/cpp/create-pivot-table/).

**C++**

{{< highlight csharp >}}

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

Además de crear nuevas tablas dinámicas, las APIs de Aspose.Cells for C++ también admiten manipular tablas dinámicas existentes. La API actualmente soporta cambiar los datos en el rango de origen de la tabla dinámica y luego actualizarla. Una vez que la tabla dinámica ha sido manipulada según sea necesario, es mejor utilizar los métodos IPivotTable.RefreshData e IPivotTable.CalculateData para actualizar la tabla dinámica contra el origen de datos actualizado.

El siguiente fragmento de código utiliza la API de Aspose.Cells for C++ para [manipular una tabla dinámica existente](/cells/es/cpp/manipulate-pivot-table/).

**C++**

{{< highlight csharp >}}

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
### **Soporte para Reglas de Formato Condicional**
Aspose.Cells for C++ ahora proporciona la capacidad de agregar reglas de formato condicional a la hoja de cálculo exponiendo la clase IFormatCondition. La clase mencionada anteriormente además proporciona los siguientes métodos para [aplicar las reglas de formato condicional](/cells/es/cpp/apply-conditional-formatting-in-worksheet/) según los requisitos de la aplicación.

- IFormatCondition.GetIAboveAverage
- IFormatCondition.GetIColorScale
- IFormatCondition.GetIDataBar
- IFormatCondition.GetIIconSet
- IFormatCondition.GetITop10

El siguiente código de ejemplo muestra cómo agregar una regla de formato condicional de tipo Valor de Celda en las celdas A1 y B2.

**C++**

{{< highlight csharp >}}

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
### **Soporte para Hipervínculos**
Aspose.Cells for C++ ahora admite [agregar hipervínculos a las celdas de la hoja de cálculo](/cells/es/cpp/add-hyperlinks-to-the-cells/). Para proporcionar esta funcionalidad, el Aspose.Cells for C++ 16.12.0 ha expuesto la clase IHyperlinkCollection, que es accesible a través del objeto IWorksheet, mientras que un hipervínculo se puede agregar a la colección utilizando el método IHyperlinkCollection.Add como se muestra a continuación.

**C++**

{{< highlight csharp >}}

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
### **Soporte para Propiedades del Documento**
La aplicación de Excel admite 2 tipos de propiedades de documento como se detalla a continuación.

- Propiedades definidas por el sistema (incorporadas): Las propiedades integradas contienen información general sobre el documento como el título del documento, nombre del autor, estadísticas del documento, etc.
- Propiedades definidas por el usuario (personalizadas): Propiedades personalizadas definidas por el usuario final en forma de par nombre-valor.

Aspose.Cells for C++ admite [gestionar ambos tipos de propiedades de documentos, integradas y personalizadas](/cells/es/cpp/managing-document-properties/). La clase IWorkbook de Aspose.Cells representa un archivo de Excel. Para acceder a las propiedades de documento integradas, utilice IWorkbook.GetBuiltInDocumentProperties, mientras que las propiedades de documento personalizadas se pueden acceder utilizando el método IWorkbook.GetCustomDocumentProperties.

El siguiente código de ejemplo carga una hoja de cálculo de muestra existente y lee las propiedades de documento integradas como Título, Asunto y la propiedad personalizada con el nombre MyCustom1.

**C++**

{{< highlight csharp >}}

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
Una tabla de Excel es una matriz de celdas que contiene cualquier número de filas y columnas, mientras que la misma tabla se denomina como un Objeto de Lista en Aspose.Cells for C++ APIs. El espacio de nombres Aspose::Cells::Tables contiene todas las clases necesarias que lidian con las operaciones relacionadas con los Objetos de Lista. Las clases más destacadas son IListObject e IListObjectCollection que permiten [crear y formatear Objetos de Lista](/cells/es/cpp/create-and-format-table/) y así sucesivamente.

El siguiente código de ejemplo carga el archivo de hoja de cálculo de muestra y luego crea un Objeto de Lista (tabla) en un rango A1:H10, y luego hace uso de sus varios métodos para mostrar el subtotal.

**C++**

{{< highlight csharp >}}

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
### **Soporte para Agrupación de Filas y Columnas**
La API Aspose.Cells for C++ se puede usar para agrupar filas y columnas mientras se usa la clase ICells que es básicamente la colección de todas las celdas en una hoja de cálculo dada. La clase ICells ofrece los métodos GroupRows y GroupColumns para [agrupar filas y columnas](/cells/es/cpp/group-rows-and-columns-of-worksheet/) respectivamente.

El siguiente fragmento de código demuestra el escenario de uso simple de ambos métodos mencionados anteriormente.

**C++**

{{< highlight csharp >}}

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
### **Soporte para Temas**
Las APIs Aspose.Cells for C++ ahora admiten usar y manipular los temas ofrecidos por la aplicación Excel.
#### **Capacidad para Aplicar Colores de Tema Personalizados**
El siguiente fragmento intenta [crear un nuevo tema con colores personalizados](/cells/es/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/) para el libro de trabajo.

**C++**

{{< highlight csharp >}}

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
#### **Soporte para Manipulación de Colores de Tema**
El siguiente código de ejemplo muestra cómo [leer y modificar los colores de tema del libro de trabajo](/cells/es/cpp/apply-custom-theme-colors-of-the-workbook-using-array-of-colors/). El código de ejemplo carga una hoja de cálculo existente, lee sus colores de tema es decir, Acento 1-Acento 6, y modifica los colores antes de guardar la hoja de cálculo.

**C++**

{{< highlight csharp >}}

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
#### **Capacidad para Copiar Temas entre Libros de Trabajo**
El siguiente código de ejemplo muestra cómo [copiar el tema de un libro de trabajo a otro](/cells/es/cpp/copy-theme-from-one-workbook-to-another/), lo cual podría ser útil para aplicar temas integrados o personalizados en múltiples hojas de cálculo.

**C++**

{{< highlight csharp >}}

 //Read excel file that has Damask theme applied on it

intrusive_ptr<IWorkbook> damask = Factory::CreateIWorkbook(damaskPath);

//Read your sample excel file

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook(samplePath);

//Copy theme from source file

wb->CopyTheme(damask);

//Save the workbook in xlsx format

wb->Save(outputPath, SaveFormat_Xlsx);

{{< /highlight >}}
## **APIs renombradas**
Con el lanzamiento de Aspose.Cells for C++ 16.12.0, hemos renombrado algunos métodos para mantener las interfaces unificadas. La lista de todas las APIs renombradas es la siguiente.
#### **Se ha renombrado el método ICell::SetStyle a ICell::SetIStyle**
#### **Se ha renombrado el método ICell::SetCharacters a ICell::SetIFontSettings**
#### **Se ha renombrado el método ICellsColor::SetThemeColor a ICellsColor::SetIThemeColor**
#### **Se ha renombrado el método ICells::SetStyle a ICells::SetIStyle**
#### **Se ha renombrado el método ICellsHelper::GetDPI_i a ICellsHelper::GetDPI**
#### **Se ha renombrado el método ICellsHelper::SetDPI_i a ICellsHelper::SetDPI**
#### **Se ha renombrado el método ICellsHelper::GetVersion_i a ICellsHelper::GetVersion**
#### **Se ha renombrado el método ICellsHelper::IsProtectedByRMS_i a ICellsHelper::IsProtectedByRMS**
#### **Se ha renombrado el método ICellsHelper::IsProtectedByRMS_i a ICellsHelper::IsProtectedByRMS**
#### **Se ha renombrado el método ICellsHelper::CellNameToIndex_i a ICellsHelper::CellNameToIndex**
#### **Se ha renombrado el método ICellsHelper::CellIndexToName_i a ICellsHelper::CellIndexToName**
#### **Se ha renombrado el método ICellsHelper::ColumnIndexToName_i a ICellsHelper::ColumnIndexToName**
#### **Se ha renombrado el método ICellsHelper::ColumnNameToIndex_i a ICellsHelper::ColumnNameToIndex**
#### **Se ha renombrado el método ICellsHelper::RowIndexToName_i a ICellsHelper::RowIndexToName**
#### **Se ha renombrado el método ICellsHelper::RowNameToIndex_i a ICellsHelper::RowNameToIndex**
#### **Se ha renombrado el método ICellsHelper::ConvertR1C1FormulaToA1_i a ICellsHelper::ConvertR1C1FormulaToA1**
#### **Se ha renombrado el método ICellsHelper::ConvertA1FormulaToR1C1_i a ICellsHelper::ConvertA1FormulaToR1C1**
#### **Se ha renombrado el método ICellsHelper::GetDateTimeFromDouble_i a ICellsHelper::GetDateTimeFromDouble**
#### **Se ha renombrado el método ICellsHelper::GetDoubleFromDateTime_i a ICellsHelper::GetDoubleFromDateTime**
#### **Se ha renombrado el método ICellsHelper::DetectLoadFormat_i a ICellsHelper::DetectLoadFormat**
#### **Se ha renombrado el método ICellsHelper::DetectFileFormat_i a ICellsHelper::DetectFileFormat**
#### **Se ha renombrado el método ICellsHelper::GetFontDir_i a ICellsHelper::GetFontDir**
#### **Se ha renombrado el método ICellsHelper::SetFontDir_i a ICellsHelper::SetFontDir**
#### **Se ha renombrado el método ICellsHelper::GetFontDirs_i a ICellsHelper::GetFontDirs**
#### **Se ha renombrado el método ICellsHelper::SetFontDirs_i a ICellsHelper::SetFontDirs**
#### **Se ha renombrado el método ICellsHelper::GetFontFiles_i a ICellsHelper::GetFontFiles**
#### **Se ha renombrado el método ICellsHelper::SetFontFiles_i a ICellsHelper::SetFontFiles**
#### **Se ha renombrado el método ICellsHelper::GetStartupPath_i a ICellsHelper::GetStartupPath**
#### **Se ha renombrado el método ICellsHelper::SetStartupPath_i a ICellsHelper::SetStartupPath**
#### **Se ha renombrado el método ICellsHelper::GetAltStartPath_i a ICellsHelper::GetAltStartPath**
#### **Se ha renombrado el método ICellsHelper::SetAltStartPath_i a ICellsHelper::SetAltStartPath**
#### **Se ha renombrado el método ICellsHelper::GetLibraryPath_i a ICellsHelper::GetLibraryPath**
#### **Se ha renombrado el método ICellsHelper::SetLibraryPath_i a ICellsHelper::SetLibraryPath**
#### **Se ha renombrado el método ICellsHelper::GetUsedColors_i a ICellsHelper::GetUsedColors**
#### **Se ha renombrado el método ICellsHelper::AddAddInFunction_i a ICellsHelper::AddAddInFunction**
#### **Se ha renombrado el método ICellsHelper::MergeFiles_i a ICellsHelper::MergeFiles**
#### **Se ha renombrado el método IColumnCollection::GetByIndex_i a IColumnCollection::GetIColumn**
#### **Se ha renombrado el método IFileFormatUtil::DetectFileFormat_i a IFileFormatUtil::DetectFileFormat**
#### **Se ha renombrado el método IFileFormatUtil::ExtensionToSaveFormat_i a IFileFormatUtil::ExtensionToSaveFormat**
#### **Se ha renombrado el método IFileFormatUtil::IsTemplateFormat_i a IFileFormatUtil::IsTemplateFormat**
#### **Se renombró el método IFileFormatUtil::LoadFormatToExtension_i a IFileFormatUtil::LoadFormatToExtension**
#### **Se renombró el método IFileFormatUtil::LoadFormatToSaveFormat_i a IFileFormatUtil::LoadFormatToSaveFormat**
#### **Se renombró el método IFileFormatUtil::SaveFormatToExtension_i a IFileFormatUtil::SaveFormatToExtension**
#### **Se renombró el método IFileFormatUtil::SaveFormatToLoadFormat_i a IFileFormatUtil::SaveFormatToLoadFormat**
#### **Se renombró el método IRange::SetStyle a IRange::SetIStyle**
#### **Se renombró el método IFindOptions::SetRange a IFindOptions::SetIRange**
#### **Se renombró el método ILoadOptions::SetLoadDataOptions a ILoadOptions::SetILoadDataOptions**
#### **Se renombró el método IWorkbook::SetSettings a IWorkbook::SetISettings**
#### **Se renombró el método IWorkbook::SetDefaultStyle a IWorkbook::SetDefaultIStyle**
{{< app/cells/assistant language="cpp" >}}
