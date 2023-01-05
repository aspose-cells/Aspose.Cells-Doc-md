---
title: ¿Por qué no abrir XML SDK?
type: docs
weight: 90
url: /es/net/why-not-open-xml-sdk/
---
{{% alert color="primary" %}}

A veces escuchamos esta pregunta:

**¿Por qué deberíamos usar los productos Aspose en lugar del SDK de Open XML gratuito?**

Esta pregunta es fácil de responder: características y funcionalidad.

{{% /alert %}}

## **¿Qué es el SDK de XML abierto?**

 De acuerdo con la[Biblioteca de MSDN](https://docs.microsoft.com/en-us/office/open-xml/open-xml-sdk?redirectedfrom=MSDN), el SDK de Open XML se define como:

"Open XML SDK 2.5 simplifica la tarea de manipular paquetes Open XML y los elementos subyacentes del esquema Open XML dentro de un paquete. Open XML SDK 2.5 encapsula muchas tareas comunes que los desarrolladores realizan en paquetes Open XML, para que pueda realizar operaciones complejas con sólo unas pocas líneas de código".

Los documentos OOXML son esencialmente archivos XML comprimidos y Open XML SDK es una colección de clases que le permite trabajar con el contenido de los documentos OOXML de una manera fuertemente tipada. Es decir, en lugar de descomprimir un archivo para extraer XML, cargar ese XML en un árbol DOM y trabajar con elementos y atributos XML directamente, Open XML SDK proporciona clases para hacerlo.

## **¿Qué es Aspose.Cells?**

Aspose.Cells es una biblioteca de clases que permite que las aplicaciones realicen las siguientes tareas de procesamiento de hojas de cálculo:

- Conversiones de alta calidad entre todos los formatos populares de Excel Microsoft, incluida la conversión a PDF, HTML, TIFF e impresión.
- Programación con un modelo de objeto de libro.
- Capacidad para crear documentos a partir de fragmentos, de uno o varios documentos, mientras se fusionan automáticamente los datos mediante formato estilístico, tablas y gráficos.
- Funciones de alto nivel, como importar datos de diferentes fuentes de datos, incluidos Array, ArrayList, DataTable / ResultSet.
- Robusto motor de cálculo de fórmulas que admite casi todas las funciones de Excel estándar y avanzadas Microsoft.

## **Comparar Open XML SDK y Aspose.Cells**

La siguiente tabla compara las características de Open XML SDK y Aspose.Cells.

|**Característica o categoría de característica**|**SDK XML abierto**|**Aspose.Cells**|
|:- |:- |:- |
|Excel compatible u otros formatos|XLSX|XLS, CSV, SpreadsheetML 2003, XLSX, HTML, delimitado por tabuladores, ODS, texto sin formato (TXT), PDF, XPS|
|Convertir entre formatos de Excel|No|Sí|
|<p>Programación de alto nivel con un modelo de objeto de libro de trabajo:</p><p>- Encontrar y reemplazar.</p><p>- Armar hojas de cálculo.</p><p>- Copie fragmentos y hojas de trabajo entre libros de trabajo.</p>|No|Sí|
|Programación detallada con un modelo de objeto de documento, acceso a elementos individuales y propiedades de formato de todos los elementos de la hoja de cálculo.|Sí|Sí|
|Acceso directo y completo de bajo nivel a los elementos y atributos XML subyacentes, como identificadores de relación, identificadores de lista de un documento OOXML.|Sí|No|
|<p>Genere informes, complete documentos con datos:</p><p>- Importar/Exportar datos a/desde una tabla de datos / _ResultSet.</p><p>- Función de marcadores inteligentes.</p><p>- Insertar/Eliminar filas/columnas/rangos.</p><p>- Fuentes de datos personalizadas.</p>|No|Sí|
|<p>Renderizado e Impresión:* Renderice páginas de la hoja de trabajo en imágenes de trama (TIFF, multipágina TIFF, PNG, JPEG, BMP).* Transforme páginas de hojas de cálculo en imágenes vectoriales (EMF).</p><p>- Convertir gráficos en imágenes (TIFF, multipágina TIFF, PNG, JPEG, BMP, EMF, etc.)</p><p>- Especificar la resolución de la imagen, la calidad, la compresión y otras opciones.</p><p>- Imprimir hojas de cálculo utilizando la infraestructura de impresión .NET. El componente tiene un método de impresión incorporado para imprimir las hojas de trabajo como se muestra en Vista previa de impresión de Microsoft Excel.</p>|No|Sí|
|Calcular/Recalcular fórmulas dinámicamente|No|Sí|
|Plataformas compatibles|Windows, .NET|Windows, Linux, Java, .NET, Mono|

Puede comparar OpenXML con Aspose.Cells Para hacer esto, le sugerimos que se familiarice con el proyecto Aspose.Cells para OpenXML: muestra cómo se pueden realizar diferentes tareas usando Aspose.Cells for .NET API versus OpenXML. El proyecto también cubre funciones para trabajar con documentos de texto que solo están disponibles en Aspose.Cells, pero no en OpenXML.

Este proyecto también es útil para los desarrolladores que buscan migrar de OpenXML a Aspose.Cells.

{{% alert color="primary" %}}

 Explorar[el complemento con ejemplos de código fuente de las características Aspose.Cells for .NET en comparación con OpenXML](https://github.com/asposemarketplace/Aspose_for_OpenXML).

 Este complemento utiliza la versión de evaluación de Aspose.Cells. Cuando esté satisfecho con su evaluación, puede comprar una licencia del[Aspose sitio web](https://purchase.aspose.com/buy) . Para eliminar el mensaje de evaluación y las limitaciones de funciones, debe solicitar una licencia de producto. Después de comprar el producto, recibirá un archivo de licencia. Siga las instrucciones en el["Licencias y suscripción"](/cells/es/net/licensing/) artículo para hacer esto.

{{% /alert %}}

**Conclusión**: Open XML SDK y Aspose.Cells no compiten cara a cara porque abordan necesidades y audiencias bastante diferentes.

## **¿Por qué no abrir XML SDK?**
Open XML SDK es una biblioteca de clases que proporciona una forma segura de trabajar con documentos OOXML. Aspose.Cells es una biblioteca de procesamiento de hojas de cálculo muy útil que brinda un excelente soporte para todos los Microsoft Excel y otros formatos de archivo.

Si todo lo que necesita hacer es una operación de programación bastante básica en un documento XLSX, Open XML SDK podría ser una opción adecuada. Con Open XML SDK, se sentirá bastante cómodo realizando tareas sencillas como generar un documento simple XLSX o eliminar comentarios, encabezados/pies de página, extraer imágenes u otros.
Algunas tareas se pueden lograr con Open XML SDK, pero no se pueden lograr con Aspose.Cells. Por ejemplo, si necesita acceder directamente a los elementos y atributos XML de un documento OOXML, debe usar Open XML SDK.

Sin embargo, si necesita realizar operaciones complejas en documentos, como algunas de las siguientes tareas, usar Aspose.Cells es su mejor opción:

- Admite otros formatos de archivo además de XLSX.
- Copie fragmentos y hojas de trabajo entre libros de trabajo o únalos de una manera que combine objetos, estilos y otros formatos de manera adecuada.
- Reemplace el texto con formato o sin formato.
- Funciones de alto nivel, como importar datos de diferentes fuentes de datos, incluidos Array, ArrayList, DataTable / ResultSet.
- Genere un documento comercial, como un pedido con los detalles del pedido desde una fuente de datos.
- Convierta un documento a PDF o XPS para que aparezca exactamente como Microsoft Excel lo habría convertido.
- Desarrolle una aplicación .NET o Java.

