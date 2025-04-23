---
title: ¿Por qué no el SDK de Open XML
type: docs
weight: 20
url: /es/java/why-not-open-xml-sdk/
---

{{% alert color="primary" %}} 

A veces escuchamos esta pregunta:

**¿Por qué deberíamos usar productos de Aspose en lugar del SDK gratuito de Open XML?**

Esta pregunta es fácil de responder: **características y funcionalidad**.

{{% /alert %}} 
## **¿Qué es Open XML SDK?**
Según la Biblioteca de MSDN, el SDK de Open XML se define como: El SDK de Open XML 2.0 simplifica la tarea de manipular paquetes Open XML y los elementos subyacentes del esquema Open XML dentro de un paquete. El SDK de Open XML 2.0 encapsula muchas tareas comunes que los desarrolladores realizan en paquetes Open XML, para que puedas realizar operaciones complejas con solo unas pocas líneas de código. Los documentos OOXML son esencialmente archivos XML comprimidos y el SDK de Open XML es una colección de clases que te permite trabajar con el contenido de los documentos OOXML de manera fuertemente tipada. En lugar de descomprimir un archivo para extraer XML, cargar ese XML en un árbol DOM y trabajar con los elementos y atributos XML directamente, el SDK de Open XML proporciona clases para hacer eso.
## **¿Qué es Aspose.Cells?**
Aspose.Cells es una biblioteca de clases que permite que tu aplicación realice las siguientes tareas de procesamiento de hojas de cálculo: Conversiones de alta calidad entre todos los formatos populares de Excel, incluyendo la conversión a PDF, HTML, TIFF e impresión. Programación con un modelo de objeto de libro de trabajo. Capacidad para construir documentos a partir de fragmentos, de uno o varios documentos, mientras se fusiona automáticamente datos mediante formato estilístico, gráficos y elementos gráficos. Funciones de alto nivel, como importar datos de diferentes fuentes de datos incluidas Array, ArrayList, DataTable / ResultSet. Motor de cálculo de fórmulas robusto que admite casi todas las funciones estándar y avanzadas de Microsoft Excel.

{{% alert color="primary" %}}
## **Comparar Open XML SDK y Aspose.Cells**
La siguiente tabla compara las características del SDK de Open XML y Aspose.Cells.

|**Característica o Categoría de Característica**|**Open XML SDK**|**Aspose.Cells**|
| :- | :- | :- |
|Formatos de Excel u otros compatibles|XLSX|XLS, CSV, SpreadsheetML 2003, XLSX, HTML, Delimitado por pestañas, ODS, Texto sin formato (TXT), PDF, XPS|
|Convertir entre formatos de Excel|No|Sí|
|<p>Programación de alto nivel con un modelo de objeto de libro de trabajo:</p><p>- Buscar y reemplazar.</p><p>- Ensamblar hojas de cálculo.</p><p>- Copiar fragmentos y hojas de cálculo entre libros de trabajo.</p>|No|Sí|
|Programación detallada con un modelo de objeto de documento, acceso a elementos individuales y propiedades de formato de todos los elementos de la hoja de cálculo.|Sí|Sí|
|Acceso directo de bajo nivel y completo a los elementos XML subyacentes y atributos como identificadores de relación, identificadores de lista de un documento OOXML.|Sí|No|
|<p>Generar informes, poblar documentos con datos:</p><p>- Importar/Exportar datos desde/hacia un *DataTable /* ResultSet.</p><p>- Función de Marcadores Inteligentes.</p><p>- Insertar/Eliminar Filas/Columnas/Rangos.</p><p>- Fuentes de datos personalizadas.</p>|No|Sí|
|<p>Renderizado e Impresión:* Renderizar páginas de hojas de cálculo a imágenes de mapa de bits (TIFF, TIFF de varias páginas, PNG, JPEG, BMP).* Renderizar páginas de hojas de cálculo a imágenes vectoriales (EMF).* Convertir gráficos a imágenes (TIFF, TIFF de varias páginas, PNG, JPEG, BMP, EMF, etc.)</p><p>- Especificar resolución de imagen, calidad, compresión y otras opciones.</p><p>- Imprimir hojas de cálculo utilizando la infraestructura de impresión .NET. El componente tiene un método de impresión incorporado para imprimir las hojas de cálculo tal como se muestra en la vista previa de impresión de MS Excel.|No|Sí|
|Calcular/Recalcular fórmulas dinámicamente|No|Sí|
|Plataformas soportadas|Windows, .NET|Windows, Linux, Java, .NET, Mono|
## **Conclusión**
  {{% alert color="primary" %}}Open XML SDK and Aspose.Cells do not compete head to head because they address quite different needs and audiences. Open XML SDK is a class library to provide a strong-typed way to work with OOXML documents. Aspose.Cells is a very useful spreadsheet processing library that provides great support for all Microsoft Excel and other file formats. If all you need to do is a fairly basic programming operation on a XLSX document, then Open XML SDK might be a suitable choice. With Open XML SDK you will be fairly comfortable doing simple tasks like generating a simple XLSX document or removing comments, headers/footers, extracting images or others. Some tasks can be achieved with Open XML SDK, but cannot be achieved with Aspose.Cells. For example, if you need to directly access the XML elements and attributes of an OOXML document, then you should use Open XML SDK.However, if you need to perform complex operations on documents, such as some of the following tasks, then using Aspose.Cells is your best option: Support other file formats in addition to XLSX. Copy fragments and worksheets between workbooks or join workbooks in a way that combines objects, styles and other formatting in an appropriate manner. Replace formatted or unformatted text. High-level functions, such as, import data from different data sources including Array, ArrayList, DataTable / ResultSet. Generate a business document, such as an order with order details from a data source. Convert a document to PDF or XPS so it appears exactly like Microsoft Excel would have converted it. Develop a .NET or Java application. {{% /alert %}}
{{< app/cells/assistant language="java" >}}
