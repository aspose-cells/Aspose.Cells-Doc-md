---
title: Comparar VSTO con Aspose.Cells for .NET
type: docs
weight: 20
url: /es/net/comparing-vsto-with-aspose-cells-for-net/
---

{{% alert color="primary" %}}

Este artículo compara el uso de VSTO (Herramientas de Visual Studio para Office) con otros enfoques para desarrollar soluciones basadas en Microsoft Office. En particular, examina Aspose.Cells y proporciona una comparación de cómo funcionan las dos soluciones. El artículo brinda información que los desarrolladores pueden usar para analizar, comparar y evaluar diferentes opciones antes de adoptar una solución.

{{% /alert %}}

## **Visión general**

Microsoft Excel es ampliamente utilizado por empresas e individuos en todo tipo de industrias. La aplicación de hojas de cálculo es prácticamente ubícua y permite a los usuarios no solo almacenar y organizar datos, sino también construir modelos complejos con fórmulas y presentar datos de manera clara con un formato avanzado y gráficos.

VSTO permite que los documentos de Microsoft Office ejecuten código envuelto en un ensamblado .NET. Se utiliza para desarrollar aplicaciones que trabajan con archivos y características de Microsoft Office. Los desarrolladores han utilizado ASP, componentes web de Office y la interoperabilidad de COM en aplicaciones durante años. Microsoft ha mejorado VSTO para facilitar el desarrollo y despliegue de aplicaciones, así como mejorar la gestión de la memoria. Pero la pregunta sigue siendo: ¿Está diseñado VSTO para ser más fácil de usar y más confiable que otros enfoques disponibles actualmente? Los desarrolladores quieren trabajar con soluciones que no les fallen en términos de rendimiento mejorado, seguridad, escalabilidad, estabilidad, confiabilidad o características.

[Aspose](http://www.aspose.com/) proporciona una excelente línea de APIs .NET, Java, Cloud y Android. Las APIs de Aspose incluyen productos como Aspose.Cells, Aspose.Words, Aspose.Pdf y Aspose.Slides, APIs que ayudan a los desarrolladores a abrir, modificar, generar, guardar, fusionar y convertir documentos en varios formatos, incluyendo XLS, XLSX, DOC, DOCX, HTML, PDF, PPT.

En este artículo, comparamos VSTO con Aspose.Cells for .NET.

[Aspose.Cells](https://products.aspose.com/cells/net/) es una API independiente de manipulación de hojas de cálculo de Microsoft Excel que lee y escribe hojas de cálculo de Microsoft Excel sin tener instalado Microsoft Excel en el cliente o en el servidor. Aspose.Cells es un componente rico en características y ofrece mucho más que solo la exportación de datos básicos. Con Aspose.Cells, los desarrolladores pueden exportar datos, formatear hojas de cálculo, importar imágenes, importar, crear y manipular gráficos, transmitir datos de Excel y guardar en varios formatos. Para obtener más información sobre el producto y sus características:

- Consulte la [documentación de Aspose.Cells](https://docs.aspose.com/cells/net/).
- Vea cómo funciona en las [demostraciones en línea](https://github.com/aspose-cells/Aspose.Cells-for-.NET).
- Pruébelo: [descargue](https://downloads.aspose.com/cells/net) una versión de evaluación de forma gratuita.

Este artículo compara VSTO y Aspose.Cells en diferentes aspectos relacionados con Microsoft Excel. La lista no es exhaustiva pero representa algunos problemas que los tomadores de decisiones deben comprender antes de tomar una decisión final antes de adoptar un enfoque.

### **Requisito del Marco de .NET**

VSTO requiere el Marco de .NET (incluida la Ejecución de Visual Studio Tools para Office SE) en el lado del cliente para ejecutar la aplicación final. En la mayoría de los entornos corporativos, especialmente en escenarios web, los usuarios finales no pueden instalar software de aplicaciones y los marcos de tiempo de ejecución relacionados. Este requisito solo hace que las aplicaciones basadas en VSTO sean problemáticas. Prácticamente descarta las aplicaciones de uso común basadas en VSTO.

Por el contrario, Aspose.Cells for .NET no exige necesariamente el Marco de .NET en el lado del cliente para el escenario subyacente. Las aplicaciones de Office construidas con el componente son livianas y garantizan trabajar en sistemas Microsoft Windows bajo carga significativa.

### **Características**

Las características que proporciona VSTO dependen de qué combinación de productos VSTO y Visual Studio tenga instalados. Las tareas comunes realizadas por VSTO para Microsoft Office Excel 2003 incluyen agregar datos a celdas, crear, abrir y guardar libros de trabajo, agregar, mover y ocultar hojas de cálculo, proteger hojas de cálculo, rangos con nombre, objeto de lista, formato de estilos, búsqueda de texto en celdas, ordenar datos, impresión y cálculos de fórmulas de Excel.

Aspose.Cells proporciona todo lo necesario para gestionar archivos de Microsoft Office Excel y mucho más. La API proporciona a los desarrolladores excelentes resultados con el menor esfuerzo. Aspose.Cells ofrece muchas funciones potentes que ahorran tiempo. La API proporciona APIs fáciles de usar para todo tipo de actividades de gestión de hojas de cálculo, cubriendo casi todas las funciones que ofrece Microsoft Excel. Todas las tareas enumeradas para VSTO pueden realizarse fácilmente con Aspose.Cells.

Aspose.Cells también admite varias funciones avanzadas, incluida la compatibilidad con marcadores inteligentes, importación y exportación de datos hacia y desde varias fuentes de datos, objetos y archivos de Excel, compatibilidad con clientes COM (cliente ASP), interoperabilidad con el componente, conversión de archivos de Excel a formato PDF, guardar gráficos y hojas de trabajo de Excel como archivos de imagen.

### **Seguridad**

Por defecto, las aplicaciones VSTO requieren permisos de Full Trust para su ejecución, ya que no permiten a los llamadores parcialmente confiables. Para restringir una aplicación web y proporcionar un nivel adicional de aislamiento de la aplicación en un entorno alojado, puede utilizar la seguridad de acceso a código para restringir los recursos a los que puede acceder la aplicación y las operaciones privilegiadas que puede realizar. Pero necesita invertir algo de tiempo y esfuerzo para comprender la seguridad de .NET.

Los Proveedores de Servicios de Internet (ISPs) que alojan múltiples aplicaciones de muchas empresas diferentes suelen utilizar el nivel de confianza medio para garantizar que las aplicaciones no puedan leer los datos entre sí ni interferir entre sí. Por razones de seguridad, los ISPs pueden limitar las aplicaciones web individuales en servidores compartidos a Confianza Parcial.

Aspose.Cells for .NET puede funcionar bajo el nivel de seguridad Medium Trust. No se requieren privilegios especiales para ejecutar el ensamblado en un entorno alojado. La confianza media impone restricciones en los tipos de recursos del sistema compartido a los que las aplicaciones pueden acceder. Muchas aplicaciones web se ejecutan en servidores de alojamiento web. En modo de alojamiento web, la mayoría de ellas solo pueden ejecutarse bajo el nivel de seguridad Medium Trust. Aspose.Cells for .NET puede satisfacer muy bien sus necesidades en este sentido.

### **Rendimiento**

El rendimiento es el factor más crítico al elegir cualquier enfoque o metodología para construir una solución.

El rendimiento de una aplicación VSTO se basa en enfoques VBA y COM según el informe de algunos usuarios. Hay varios factores que influyen en el rendimiento de VSTO, y es importante poner estos factores en perspectiva.

- El costo de arranque de .NET es inherentemente caro. Las aplicaciones escritas con .NET deben incurrir en los gastos de la compilación Just-In-Time (JIT), por lo que la compilación JIT no se puede evitar.
- Otro factor de rendimiento que influye en las aplicaciones basadas en VSTO tiene que ver con el gasto de llamar a través de las espesas capas de automatización que envuelven los objetos COM de Microsoft Office. VBA, construido y optimizado para interactuar con Microsoft Office, tiene una distancia más corta que recorrer que .NET.
- Por último, alojar objetos de Excel en el IDE de Visual Studio es costoso en términos de recursos. Las aplicaciones VSTO tienen una huella de memoria más grande que las aplicaciones VBA. Las aplicaciones de Excel de VSTO utilizan mucha memoria y nunca la liberan de vuelta al sistema operativo hasta que se cierren todas las instancias de Microsoft Excel.

Si está considerando adoptar VSTO como plataforma de desarrollo para la tecnología de Microsoft Office, dedique tiempo a familiarizarse con estos atributos.

Además, la implicación de rendimiento de siempre verificar actualizaciones puede no ser apropiada para la solución (servidores de implementación más lentos, conexiones de red más lentas o simplemente incapacidad para alcanzar el servidor con frecuencia pueden impactar negativamente los tiempos de carga).

En contraste, Aspose.Cells for .NET es altamente escalable, flexible y rápido. Generalmente, las aplicaciones de Office no fueron diseñadas para ser utilizadas simultáneamente por cientos o miles de usuarios; sin embargo, Aspose.Cells sí lo fue. La API es estable y puede realizar tareas de hojas de cálculo perfectamente ya sea en un solo servidor, impulsando una aplicación única o en una granja web equilibrada que impulsa una aplicación empresarial.

### **Requisitos del sistema**

Al analizar los requisitos del sistema para estos dos enfoques, encontramos que VSTO es más costoso y necesita más elementos esenciales.

VSTO tiene una larga lista de requisitos previos:

- **Sistemas operativos compatibles**: Windows 2000; Windows Server 2003; Windows Vista; Windows XP
- **Versiones del marco .NET compatibles**: solo .NET Framework 2.0 o superior.
- Una o más de las siguientes ediciones de Visual Studio Tools para Office:
  - Microsoft Visual Studio 2005 Tools for the Microsoft Office System
  - Microsoft Visual Studio 2005 Tools for the 2007 Microsoft Office System
  - Edición Profesional de Visual Studio 2008
  - Edición de Team Suite de Visual Studio 2008
  - Una versión de Microsoft Office:
  - Microsoft Office Professional 2003 SP1
  - Sistema 2007 de Microsoft Office

Aspose.Cells no requiere que Microsoft Excel esté instalado en el cliente o en el servidor, ya que es un motor de creación de hojas de cálculo. Sin embargo, para ver documentos de Microsoft Excel, necesitas al menos el Visor de Microsoft Excel instalado en el sistema.

- **Sistemas operativos compatibles**: Windows 2000; Windows Server 2003; Windows Vista; Windows XP
- **Versiones de .NET Framework admitidas**: Se admiten todas las versiones de .NET Framework, 1.0, 1.1, 2.0, 3.x, etc.

### **Instalación y despliegue**

Instalar VSTO puede ser una tarea grande y problemática. En ocasiones, una instalación exige que reinstales manualmente aspectos de las herramientas y los registres manualmente también. Puede volverse complicado.

Por otro lado, Aspose.Cells for .NET está empaquetado en un solo DLL, por lo que no es necesario instalar aplicaciones adicionales. El componente es solo utilizado por aplicaciones .NET y ninguna parte del código del componente está diseñada para esperar una respuesta humana. Simplemente visita la [página de descargas de Aspose.Cells](https://downloads.aspose.com/cells/net) y descarga el instalador más reciente de Aspose.Cells. Ejecuta el archivo descargado y sigue las instrucciones del instalador. Luego, para usar el componente, haz referencia a él en tu proyecto.

## **Tarea de ejemplo**

Para mostrar las diferencias entre los dos enfoques, el código a continuación muestra cómo usar las API de VSTO y Aspose.Cells para completar un archivo de plantilla con datos.

1. Se utiliza un archivo de Microsoft Excel (TempBook.xls) como plantilla.
   El libro de trabajo contiene algunas hojas de cálculo con algunas celdas rellenas con datos.
1. El código de ejemplo coloca 1000*20 registros en la primera hoja de cálculo del archivo de Excel de plantilla.
   La hoja de cálculo se llena con datos constantes (falsos) en las celdas.

La tarea se realiza en un sistema con Intel(R) Celeron(R) CPU 2.40 GHz, 760 MB de RAM en el sistema operativo Microsoft Windows XP Professional.

Los segmentos de código a continuación ilustran cómo realizar estas tareas con cada API.

### **Código de VSTO**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-ComparingVSTOWithAspose-VSTOCode-1.cs" >}}

### **Código de Aspose.Cells**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-KnowledgeBase-ComparingVSTOWithAspose-UsingAsposeCells-1.cs" >}}

### **Resultados**

Los resultados mostraron que el uso de la API VSTO tardó aproximadamente 2.5 minutos (más de 150 segundos) en completar la tarea, mientras que Aspose.Cells tardó menos de 1 segundo en un hardware común con configuraciones de sistema normales.

Si el bucle se extiende, por ejemplo para completar 10,000*20 celdas, Aspose.Cells tarda aproximadamente 5.5 segundos en realizar el trabajo.

## **Conclusión**

Si estás considerando usar una tecnología de Microsoft Office en una solución empresarial, primero familiarízate con las alternativas disponibles. Realiza algunas pruebas basadas en diferentes productos y expónlos a una variedad de condiciones del mundo real, como cargas y estrés, para ver cómo se desempeñan.

Aspose.Cells es un producto estable y maduro con una base de clientes en todo el mundo, y lo suficientemente escalable como para funcionar bien bajo cargas pesadas.

El rendimiento de VSTO aún no está refinado. Es bastante posible que algunos de estos problemas de rendimiento no estén relacionados directamente con VSTO, sino que tengan conexiones con los procesos de compilación JIT de .NET. Aun así, existen ciertas dudas sobre si las aplicaciones de VSTO se escalarían a medida que aumentara la carga. El nuevo modelo de VSTO no requiere que Excel resida en el servidor web para el procesamiento de documentos, pero creo que VSTO tiene un largo camino por recorrer para lograr un impacto real.
{{< app/cells/assistant language="csharp" >}}
