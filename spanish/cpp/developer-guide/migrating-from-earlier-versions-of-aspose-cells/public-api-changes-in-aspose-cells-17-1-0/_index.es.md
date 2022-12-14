---
title: Público API Cambios en Aspose.Cells 17.1.0
type: docs
weight: 20
url: /es/cpp/public-api-changes-in-aspose-cells-17-1-0/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 16.12.0 a la 17.1.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Compatibilidad con rangos con nombre**
 Aspose.Cells para C++ ahora admite la creación y la manipulación de rangos con nombre. El siguiente fragmento de código demuestra lo simple que es usar Aspose.Cells para C++ API para[crear rangos con nombre](/cells/es/cpp/create-named-range-in-a-workbook/).

**C++**

{{< highlight "csharp" >}}

 //Path of your directory where you want to read or write files from

StringPtr dirPath = new String("D:\\Downloads\\");

//Path of output excel file

StringPtr outCreateNamedRange = (new String(dirPath))->Append(new String("outCreateNamedRange.xlsx"));

//Create a workbook

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook();

//Access first worksheet

intrusive_ptr<IWorksheet> ws = wb->GetIWorksheets()->GetObjectByIndex(0);

//Create a range

intrusive_ptr<IRange> rng = ws->GetICells()->CreateIRange((intrusive_ptr<String>)new String("A5:C10"));

//Set its name to make it named range

rng->SetName((intrusive_ptr<String>)new String("MyNamedRange"));

//Read the named range created above from names collection

intrusive_ptr<IName> nm = wb->GetIWorksheets()->GetINames()->GetObjectByIndex(0);

//Print its FullText and RefersTo properties

printf("Full Text: %s\n", nm->GetFullText()->charValue());

printf("Refers To: %s\n", nm->GetRefersTo()->charValue());

//Save the workbook in xlsx format

wb->Save(outCreateNamedRange, SaveFormat_Xlsx);

{{< /highlight >}}

 Además de crear nuevos rangos con nombre, las API Aspose.Cells para C++ también admiten la manipulación de rangos con nombre existentes. El siguiente fragmento de código usa Aspose.Cells para C++ API para[manipular un rango con nombre existente](/cells/es/cpp/manipulate-named-range-in-a-workbook/).

**C++**

{{< highlight "csharp" >}}

 //Path of your directory where you want to read or write files from

StringPtr dirPath = new String("D:\\Downloads\\");

//Path of source excel file

StringPtr srcManipulateRange = (new String(dirPath))->Append(new String("srcManipulateRange.xlsx"));

//Path of output excel file

StringPtr outManipulateRange = (new String(dirPath))->Append(new String("outManipulateRange.xlsx"));

//Create a workbook

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook(srcManipulateRange);

//Read the named range created above from names collection

intrusive_ptr<IName> nm = wb->GetIWorksheets()->GetINames()->GetObjectByIndex(0);

//Print its FullText and RefersTo properties

printf("Full Text: %s\n", nm->GetFullText()->charValue());

printf("Refers To: %s\n", nm->GetRefersTo()->charValue());

//Manipulate the RefersTo property of NamedRange

nm->SetRefersTo((intrusive_ptr<String>)new String("=Sheet1!$D$5:$J$10"));

//Save the workbook in xlsx format

wb->Save(outManipulateRange, SaveFormat_Xlsx);

{{< /highlight >}}
### **Se agregó el método ICells::LinkToXmlMap**
El método LinkToXmlMap se ha agregado a la clase ICells, que es útil para vincular un mapa XML.
### **Agregado método ICells::ImportCSV**
El método ImportCSV se ha agregado a la clase ICells, que es útil para importar un archivo CSV a las celdas de una hoja de trabajo.
### **Se agregó el método ICells::ImportTwoDimensionArray**
El método GetIProtectedRangeCollection se ha agregado a la clase ICells, que es útil para importar una matriz bidimensional de datos en una hoja de trabajo.
### **Se agregó el método IWorksheet::GetIProtectedRangeCollection**
El método GetIProtectedRangeCollection se agregó a la clase IWorksheet, que es útil para recuperar la colección de objetos IProtectedRange.
### **Se agregó el método IWorksheet::GetIProtectedRangeCollection**
El método GetIProtectedRangeCollection se ha agregado a la clase IWorksheet, que es útil para recuperar la colección de rangos de edición de la hoja de cálculo.
### **Se agregó el método IWorkbookSettings::ClearPivottables**
El método ClearPivottables se agregó a la clase IWorkbookSettings, que es útil para borrar todas las tablas dinámicas de una hoja de cálculo determinada.
### **Se agregó el método IWorksheetCollection::CreateIRange**
El método CreateIRange se ha agregado a la clase IWorksheetCollection, que es útil para crear un objeto de IRange pasando referencias de celdas en formato de cadena.
### **Se agregó el método IExternalLink::IsVisible**
El método IsVisible obtiene el estado de visibilidad de un enlace externo en la aplicación de Excel.
### **Se agregaron los métodos GetScaleCrop y SetScaleCrop**
Aspose.Cells para C++ 17.1.0 ha expuesto los métodos GetScaleCrop y SetScaleCrop a la clase IBuiltInDocumentPropertyCollection. Estos métodos son útiles para obtener o establecer la propiedad ScaleCrop que indica el modo de visualización de la miniatura del documento.
### **Se agregaron los métodos GetLinksUpToDate y SetLinksUpToDate**
Aspose.Cells para C++ 17.1.0 ha expuesto los métodos GetLinksUpToDate y SetLinksUpToDate a la clase IBuiltInDocumentPropertyCollection. Estos métodos son útiles para obtener o establecer la propiedad LinkUpToDate que indica si los hipervínculos de un documento están actualizados.
### **Se agregaron los métodos GetAbsolutePath y SetAbsolutePath**
Aspose.Cells para C++ 17.1.0 ha expuesto los métodos GetAbsolutePath y SetAbsolutePath a la clase IWorkbook. Estos métodos son útiles para obtener o establecer la ruta absoluta del archivo que solo se puede usar para enlaces externos.
### **Métodos GetFormula y SetFormula agregados**
Esta versión de Aspose.Cells para C++ ha expuesto los métodos GetFormula y SetFormula para la clase IListColumn. Estos métodos son útiles para obtener o establecer la fórmula de una columna de lista.
### **Se agregaron los métodos GetCheckCompatibility y SetCheckCompatibility**
Esta versión de Aspose.Cells para C++ ha expuesto los métodos GetCheckCompatibility y GetCheckCompatibility para la clase IWorkbookSettings. Estos métodos son útiles para obtener o establecer la propiedad de verificación de compatibilidad que indica si API debe verificar la compatibilidad al guardar el libro de trabajo. El valor predeterminado es verdadero y se puede establecer en falso si el requisito de la aplicación no es verificar la compatibilidad.
### **Se agregaron los métodos GetILightCellsDataHandler y SetILightCellsDataHandler**
Aspose.Cells para C++ ahora ha expuesto los métodos GetILightCellsDataHandler y SetILightCellsDataHandler para la clase ILoadOptions. Estos métodos denotan el controlador de datos para procesar datos de celdas mientras se lee el archivo de plantilla.
### **Se agregaron los métodos GetCultureInfo y SetCultureInfo**
Aspose.Cells para C++ ha expuesto los métodos GetCultureInfo y SetCultureInfo para la clase ILoadOptions. Estos métodos pueden obtener o configurar la información cultural del sistema en el momento de la carga del archivo.
## **API eliminadas**
### **Método ICells::MaxDataRowInColumn eliminado**
Se recomienda utilizar el método ICells::GetLastDataRow en su lugar.
### **Se eliminó el método ICell::GetConditionalIStyle**
Se recomienda utilizar el método ICell::GetIConditionalFormattingResult en su lugar.
### **Se eliminaron los métodos IPageSetup::GetDraft y SetDraft**
Se recomienda utilizar los métodos IPageSetup::GetPrintDraft & IPageSetup::SetPrintDraft en su lugar.

{{% alert color="primary" %}} 

Con el lanzamiento de Aspose.Cells para C++ 17.1.0, hemos eliminado algunos métodos que no estaban en uso, por lo que se consideraron innecesarios. Aquí está la lista de todos estos métodos.

- Métodos IPaneCollection::GetAcitvePaneType y SetAcitvePaneType
- Método IRange::ToString
- Método IRow::Equals
- IWorkbook::Método SetISettings
- Método ICell::ToString()
- Método ICell::Equals(ObjectPtr)
- Método ICell::GetHashCode
- Método IWorksheet::ToString

{{% /alert %}}
