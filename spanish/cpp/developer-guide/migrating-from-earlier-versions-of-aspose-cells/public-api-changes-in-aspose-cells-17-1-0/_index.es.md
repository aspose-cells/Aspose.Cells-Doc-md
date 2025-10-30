---
title: Cambios en la API pública en Aspose.Cells 17.1.0
type: docs
weight: 20
url: /es/cpp/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 16.12.0 hasta la 17.1.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo nuevos y actualizados métodos públicos, clases añadidas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Soporte para Rangos Nombrados**
Aspose.Cells for C++ ahora es compatible con la creación y manipulación de Rangos Nombrados. El siguiente fragmento de código demuestra lo sencillo que es usar la API Aspose.Cells for C++ para [crear rangos nombrados](/cells/es/cpp/create-named-range-in-a-workbook/).

**C++**

{{< highlight csharp >}}

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

Además de crear nuevos Rangos Nombrados, las APIs Aspose.Cells for C++ también admiten manipular Rangos Nombrados existentes. El siguiente fragmento de código utiliza la API Aspose.Cells for C++ para [manipular un rango nombrado existente](/cells/es/cpp/manipulate-named-range-in-a-workbook/).

**C++**

{{< highlight csharp >}}

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
Se ha agregado el método LinkToXmlMap a la clase ICells, que es útil para vincular un mapa XML.
### **Se agregó el método ICells::ImportCSV**
Se ha añadido el método ImportCSV a la clase ICells que es útil para importar un archivo CSV en las celdas de una hoja de cálculo.
### **Añadido método ICells::ImportTwoDimensionArray**
Se ha añadido el método GetIProtectedRangeCollection a la clase ICells que es útil para importar un array de datos bidimensional en una hoja de cálculo.
### **Añadido método IWorksheet::GetIProtectedRangeCollection**
Se ha añadido el método GetIProtectedRangeCollection a la clase IWorksheet que es útil para recuperar la colección de objetos IProtectedRange.
### **Añadido método IWorksheet::GetIProtectedRangeCollection**
Se ha añadido el método GetIProtectedRangeCollection a la clase IWorksheet que es útil para recuperar la colección de rangos de edición de la hoja de cálculo.
### **Añadido método IWorkbookSettings::ClearPivottables**
Se ha añadido el método ClearPivottables a la clase IWorkbookSettings que es útil para borrar todas las tablas dinámicas de una hoja de cálculo específica.
### **Añadido método IWorksheetCollection::CreateIRange**
Se ha añadido el método CreateIRange a la clase IWorksheetCollection que es útil para crear un objeto de tipo IRange mediante la introducción de referencias de celdas en formato de cadena.
### **Añadido método IExternalLink::IsVisible**
El método IsVisible obtiene el estado de visibilidad de un enlace externo en la aplicación de Excel.
### **Añadidos métodos GetScaleCrop & SetScaleCrop**
Se ha expuesto en Aspose.Cells for C++ 17.1.0 los métodos GetScaleCrop & SetScaleCrop en la clase IBuiltInDocumentPropertyCollection. Estos métodos son útiles para obtener o establecer la propiedad ScaleCrop que indica el modo de visualización de la miniatura del documento.
### **Añadidos métodos GetLinksUpToDate & SetLinksUpToDate**
Se ha expuesto en Aspose.Cells for C++ 17.1.0 los métodos GetLinksUpToDate & SetLinksUpToDate en la clase IBuiltInDocumentPropertyCollection. Estos métodos son útiles para obtener o establecer la propiedad LinkUpToDate que indica si los hipervínculos en un documento están actualizados.
### **Añadidos métodos GetAbsolutePath & SetAbsolutePath**
Se ha expuesto en Aspose.Cells for C++ 17.1.0 los métodos GetAbsolutePath & SetAbsolutePath en la clase IWorkbook. Estos métodos son útiles para obtener o establecer la ruta absoluta del archivo que solo se puede utilizar para enlaces externos.
### **Añadidos métodos GetFormula & SetFormula**
Esta versión de Aspose.Cells for C++ ha expuesto los métodos GetFormula y SetFormula para la clase IListColumn. Estos métodos son útiles para obtener o establecer la fórmula de una columna de lista.
### **Añadidos los métodos GetCheckCompatibility y SetCheckCompatibility.**
Esta versión de Aspose.Cells for C++ ha expuesto los métodos GetCheckCompatibility y GetCheckCompatibility para la clase IWorkbookSettings. Estos métodos son útiles para obtener o establecer la propiedad de comprobación de compatibilidad que indica si la API debe verificar la compatibilidad al guardar el libro de trabajo. El valor predeterminado es verdadero y se puede establecer en falso si el requisito de la aplicación no es verificar la compatibilidad.
### **Añadidos los métodos GetILightCellsDataHandler y SetILightCellsDataHandler.**
Aspose.Cells for C++ ha expuesto los métodos GetILightCellsDataHandler y SetILightCellsDataHandler para la clase ILoadOptions. Estos métodos denotan el controlador de datos para procesar los datos de las celdas al leer el archivo de plantilla.
### **Añadidos los métodos GetCultureInfo y SetCultureInfo.**
Aspose.Cells for C++ ha expuesto los métodos GetCultureInfo y SetCultureInfo para la clase ILoadOptions. Estos métodos pueden obtener o establecer la información de la cultura del sistema en el momento de la carga del archivo.
## **APIs Eliminadas**
### **Eliminado el método ICells::MaxDataRowInColumn.**
Se recomienda utilizar el método ICells::GetLastDataRow en su lugar.
### **Eliminado el método ICell::GetConditionalIStyle.**
Se recomienda utilizar el método ICell::GetIConditionalFormattingResult en su lugar.
### **Eliminados los métodos IPageSetup::GetDraft y SetDraft.**
Se recomienda utilizar los métodos IPageSetup::GetPrintDraft e IPageSetup::SetPrintDraft en su lugar.

{{% alert color="primary" %}} 

Con la versión Aspose.Cells for C++ 17.1.0, hemos eliminado algunos métodos que no se estaban utilizando y, por lo tanto, se consideraban innecesarios. Aquí está la lista de todos esos métodos.

- Métodos IPaneCollection::GetAcitvePaneType y SetAcitvePaneType
- Método IRange::ToString
- Método IRow::Equals
- Método IWorkbook::SetISettings
- Método ICell::ToString()
- Método ICell::Equals(ObjectPtr)
- Método ICell::GetHashCode
- Método IWorksheet::ToString

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
