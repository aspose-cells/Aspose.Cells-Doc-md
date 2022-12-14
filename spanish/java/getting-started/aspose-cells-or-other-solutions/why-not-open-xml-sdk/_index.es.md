---
title: ¿Por qué no abrir XML SDK?
type: docs
weight: 20
url: /es/java/why-not-open-xml-sdk/
---
{{% alert color="primary" %}} 

A veces escuchamos esta pregunta:

**¿Por qué deberíamos usar los productos Aspose en lugar del SDK de Open XML gratuito?**

 Esta pregunta es fácil de responder:**caracteristicas y funcionalidad**.

{{% /alert %}} 
## ** ¿Qué es el SDK de XML abierto?**
Según MSDN Library, Open XML SDK se define como: Open XML SDK 2.0 simplifica la tarea de manipular paquetes Open XML y los elementos subyacentes del esquema Open XML dentro de un paquete. Open XML SDK 2.0 encapsula muchas tareas comunes que los desarrolladores realizan en paquetes Open XML, para que pueda realizar operaciones complejas con solo unas pocas líneas de código. Los documentos OOXML son esencialmente archivos XML comprimidos y Open XML SDK es una colección de clases que permite le permite trabajar con el contenido de los documentos OOXML de una manera fuertemente tipada. Es decir, en lugar de descomprimir un archivo para extraer XML, cargar ese XML en un árbol DOM y trabajar con elementos y atributos XML directamente, Open XML SDK proporciona clases para hacerlo.
## ** ¿Qué es Aspose.Cells?**
Aspose.Cells es una biblioteca de clases que permite que su aplicación realice las siguientes tareas de procesamiento de hojas de cálculo: Conversiones de alta calidad entre todos los formatos populares de Excel, incluida la conversión a PDF, HTML, TIFF e impresión. Programación con un modelo de objeto de libro. Capacidad para crear documentos a partir de fragmentos, de uno o varios documentos, mientras se fusionan automáticamente los datos mediante formato estilístico, tablas y gráficos. Funciones de alto nivel, como importar datos de diferentes fuentes de datos, incluidos Array, ArrayList, DataTable / ResultSet. Robusto motor de cálculo de fórmulas que admite casi todas las funciones de Excel estándar y avanzadas Microsoft.

{{% alert color="primary" %}}
## ** Comparar Open XML SDK y Aspose.Cells**
 La siguiente tabla compara las características de Open XML SDK y Aspose.Cells.{{% /alert %}}

|**Característica o categoría de característica**|**SDK XML abierto**|**Aspose.Cells**|
|:- |:- |:- |
|Excel compatible u otros formatos|XLSX|XLS, CSV, SpreadsheetML 2003, XLSX, HTML, delimitado por tabuladores, ODS, texto sin formato (TXT), PDF, XPS|
|Convertir entre formatos de Excel|No|Sí|
|<p>Programación de alto nivel con un modelo de objeto de libro de trabajo:</p><p>- Encontrar y reemplazar.</p><p>- Armar hojas de cálculo.</p><p>- Copie fragmentos y hojas de trabajo entre libros de trabajo.</p>|No|Sí|
|Programación detallada con un modelo de objeto de documento, acceso a elementos individuales y propiedades de formato de todos los elementos de la hoja de cálculo.|Sí|Sí|
|Acceso directo y completo de bajo nivel a los elementos y atributos XML subyacentes, como identificadores de relación, identificadores de lista de un documento OOXML.|Sí|No|
|<p>Genere informes, complete documentos con datos:</p><p>- Importar/Exportar datos a/desde un*Tabla de datos /*Conjunto resultante.</p><p>- Función de marcadores inteligentes.</p><p>- Insertar/Eliminar Filas/Columnas/Rangos.</p><p>- Fuentes de datos personalizadas.</p>|No|Sí|
|<p>Renderizado e Impresión:* Renderice páginas de hojas de trabajo en imágenes rasterizadas (TIFF, TIFF de varias páginas, PNG, JPEG, BMP).*Renderice páginas de hojas de cálculo en imágenes vectoriales (EMF).* Convierta gráficos en imágenes (TIFF, TIFF de varias páginas, PNG, JPEG, BMP, EMF, etc.)</p><p>- Especifique la resolución, la calidad, la compresión y otras opciones de la imagen. </p><p>- Imprimir hojas de cálculo utilizando la infraestructura de impresión .NET. El componente tiene un método de impresión incorporado para imprimir las hojas de trabajo como se muestra en la vista previa de impresión de MS Excel.</p>|No|Sí|
|Calcular/Recalcular fórmulas dinámicamente| No| Sí|
|Plataformas compatibles|Windows, .NET|Windows, Linux, Java, .NET, Mono|
## **Conclusión**
  {{% alert color="primary" %}}Open XML SDK y Aspose.Cells no compiten cara a cara porque abordan necesidades y audiencias bastante diferentes. Open XML SDK es una biblioteca de clases que proporciona una forma segura de trabajar con documentos OOXML. Aspose.Cells es una biblioteca de procesamiento de hojas de cálculo muy útil que brinda un excelente soporte para todos los Microsoft Excel y otros formatos de archivo. Si todo lo que necesita hacer es una operación de programación bastante básica en un documento XLSX, Open XML SDK podría ser una opción adecuada. Con Open XML SDK se sentirá bastante cómodo realizando tareas sencillas como generar un documento XLSX sencillo o eliminar comentarios, encabezados/pies de página, extraer imágenes u otros. Algunas tareas se pueden lograr con Open XML SDK, pero no se pueden lograr con Aspose.Cells. Por ejemplo, si necesita acceder directamente a los elementos y atributos XML de un documento OOXML, debe usar Open XML SDK. Sin embargo, si necesita realizar operaciones complejas en documentos, como algunas de las siguientes tareas, entonces usar Aspose.Cells es su mejor opción: admitir otros formatos de archivo además de XLSX. Copie fragmentos y hojas de trabajo entre libros de trabajo o únalos de una manera que combine objetos, estilos y otros formatos de manera adecuada. Reemplace el texto con formato o sin formato. Funciones de alto nivel, como importar datos de diferentes fuentes de datos, incluidos Array, ArrayList, DataTable / ResultSet. Genere un documento comercial, como un pedido con los detalles del pedido desde una fuente de datos. Convierta un documento a PDF o XPS para que aparezca exactamente como Microsoft Excel lo habría convertido. Desarrolle una aplicación .NET o Java.{{% /alert %}}
