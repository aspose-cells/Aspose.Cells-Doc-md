---
title: ¿Por qué no el SDK de Open XML
type: docs
weight: 90
url: /es/net/why-not-open-xml-sdk/
---

{{% alert color="primary" %}}

A veces escuchamos esta pregunta:

**¿Por qué deberíamos usar productos de Aspose en lugar del SDK gratuito de Open XML?**

Esta pregunta es fácil de responder: características y funcionalidad.

{{% /alert %}}

## **¿Qué es Open XML SDK?**

Según la [Biblioteca de MSDN](https://docs.microsoft.com/en-us/office/open-xml/open-xml-sdk?redirectedfrom=MSDN), el Open XML SDK se define como:

"El Open XML SDK 2.5 simplifica la tarea de manipular paquetes Open XML y los elementos de esquema Open XML subyacentes dentro de un paquete. El Open XML SDK 2.5 encapsula muchas tareas comunes que realizan los desarrolladores en paquetes Open XML, para que pueda realizar operaciones complejas con solo unas pocas líneas de código."

Los documentos OOXML son básicamente archivos XML comprimidos y Open XML SDK es una colección de clases que le permite trabajar con el contenido de los documentos OOXML de una manera fuertemente tipada. En lugar de descomprimir un archivo para extraer XML, cargar ese XML en un árbol DOM y trabajar directamente con los elementos y atributos XML, Open XML SDK proporciona clases para hacer eso.

## **¿Qué es Aspose.Cells?**

Aspose.Cells es una biblioteca de clases que permite a las aplicaciones realizar las siguientes tareas de procesamiento de hojas de cálculo:

- Conversiones de alta calidad entre todos los formatos populares de Microsoft Excel, incluida la conversión a PDF, HTML, TIFF e impresión.
- Programación con un modelo de objeto de libro de trabajo.
- Capacidad para construir documentos a partir de fragmentos, de uno o varios documentos, mientras se fusiona automáticamente datos mediante formato estilístico, gráficos y gráficos.
- Funciones de alto nivel, como importar datos de diferentes fuentes de datos, incluidos Array, ArrayList, DataTable/ResultSet.
- Robusto motor de cálculo de fórmulas que admite casi todas las funciones estándar y avanzadas de Microsoft Excel.

## **Comparar Open XML SDK y Aspose.Cells**

La siguiente tabla compara las características del Aspose.Cells y del SDK de Open XML.

|**Característica o Categoría de Característica**|**Open XML SDK**|**Aspose.Cells**|
| :- | :- | :- |
|Formatos de Excel u otros compatibles|XLSX|XLS, CSV, SpreadsheetML 2003, XLSX, HTML, Delimitado por pestañas, ODS, Texto sin formato (TXT), PDF, XPS|
|Convertir entre formatos de Excel|No|Sí|
|<p>Programación de alto nivel con un modelo de objeto de libro de trabajo:</p><p>- Buscar y reemplazar.</p><p>- Ensamblar hojas de cálculo.</p><p>- Copiar fragmentos y hojas de cálculo entre libros de trabajo.</p>|No|Sí|
|Programación detallada con un modelo de objeto de documento, acceso a elementos individuales y propiedades de formato de todos los elementos de la hoja de cálculo.|Sí|Sí|
|Acceso directo de bajo nivel y completo a los elementos XML subyacentes y atributos como identificadores de relación, identificadores de lista de un documento OOXML.|Sí|No|
|<p>Generar informes, poblar documentos con datos:</p><p>- Importar/Exportar datos desde/hacia un DataTable / ResultSet.</p><p>- Función de Marcadores Inteligentes.</p><p>- Insertar/Eliminar Filas/Columnas/Rangos.</p><p>- Fuentes de datos personalizadas.</p>|No|Sí|
|<p>Renderizado e impresión:* Renderizar páginas de hojas de cálculo como imágenes de mapa de bits (TIFF, TIFF multipágina, PNG, JPEG, BMP).* Renderizar páginas de hojas de cálculo como imágenes vectoriales (EMF).</p><p>- Convertir gráficos a imágenes (TIFF, TIFF multipágina, PNG, JPEG, BMP, EMF, etc.)</p><p>- Especificar resolución de imagen, calidad, compresión y otras opciones.</p><p>- Imprimir hojas de cálculo usando la infraestructura de impresión de .NET. El componente tiene un método de impresión incorporado para imprimir las hojas de cálculo como se muestra en la vista previa de impresión de Microsoft Excel.</p>|No|Sí|
|Calcular/Recalcular fórmulas dinámicamente|No|Sí|
|Plataformas soportadas|Windows, .NET|Windows, Linux, Java, .NET, Mono|

Puede comparar OpenXML con Aspose.Cells. Para hacerlo, le sugerimos que se familiarice con el proyecto Aspose.Cells for OpenXML, que muestra cómo se pueden realizar diferentes tareas utilizando la API Aspose.Cells for .NET en comparación con OpenXML. El proyecto también cubre características para trabajar con documentos de texto que solo están disponibles en Aspose.Cells, pero no en OpenXML.

Este proyecto también es útil para desarrolladores que buscan migrar de OpenXML a Aspose.Cells.

{{% alert color="primary" %}}

Explore el [complemento con ejemplos de código fuente de Aspose.Cells for .NET características en comparación con OpenXML](https://github.com/asposemarketplace/Aspose_for_OpenXML).

Este complemento utiliza la versión de evaluación de Aspose.Cells. Cuando esté satisfecho con su evaluación, puede adquirir una licencia en el [sitio web de Aspose](https://purchase.aspose.com/buy). Para eliminar el mensaje de evaluación y las limitaciones de funciones, debe aplicar una licencia de producto. Después de comprar el producto, recibirá un archivo de licencia. Siga las instrucciones en el artículo ["Licencia y Suscripción"](/cells/es/net/licensing/) para hacerlo.

{{% /alert %}}

**Conclusión**: El SDK de Open XML y Aspose.Cells no compiten directamente porque abordan necesidades y audiencias bastante diferentes.

## **¿Por qué no usar Open XML SDK?**
El SDK de Open XML es una biblioteca de clases que proporciona una forma fuertemente tipada de trabajar con documentos OOXML. Aspose.Cells es una biblioteca de procesamiento de hojas de cálculo muy útil que brinda un gran soporte para todos los formatos de archivo de Microsoft Excel y otros.

Si todo lo que necesita hacer es una operación de programación bastante básica en un documento XLSX, entonces el SDK de Open XML podría ser una opción adecuada. Con el SDK de Open XML, estará bastante cómodo realizando tareas simples como generar un documento XLSX simple o eliminar comentarios, encabezados/pies de página, extraer imágenes u otros. 
Algunas tareas se pueden lograr con el SDK de Open XML, pero no con Aspose.Cells. Por ejemplo, si necesita acceder directamente a los elementos y atributos XML de un documento OOXML, entonces debe usar el SDK de Open XML.

Sin embargo, si necesita realizar operaciones complejas en documentos, como algunas de las siguientes tareas, entonces usar Aspose.Cells es su mejor opción:

- Soporte para otros formatos de archivo además de XLSX.
- Copiar fragmentos y hojas de cálculo entre libros de trabajo o unir libros de trabajo de manera que combine objetos, estilos y otros formatos de manera apropiada.
- Reemplazar texto formateado o sin formato.
- Funciones de alto nivel, como importar datos de diferentes fuentes de datos, incluidos Array, ArrayList, DataTable/ResultSet.
- Generar un documento comercial, como un pedido con detalles del pedido de una fuente de datos.
- Convertir un documento a PDF o XPS para que aparezca exactamente como lo habría convertido Microsoft Excel.
- Desarrollar una aplicación .NET o Java.

