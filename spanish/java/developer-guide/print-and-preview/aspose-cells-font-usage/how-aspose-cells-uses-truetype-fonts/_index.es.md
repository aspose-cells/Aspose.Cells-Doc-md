---
title: Cómo Aspose.Cells utiliza las fuentes TrueType
type: docs
weight: 10
url: /es/java/how-aspose-cells-uses-truetype-fonts/
---

{{% alert color="primary" %}}

Aspose.Cells requiere fuentes TrueType al renderizar hojas de cálculo a formatos como PDF, XPS e imágenes.

Cuando Aspose.Cells renderiza una hoja de cálculo, requiere acceso a las fuentes TrueType utilizadas en la hoja de cálculo. Esta es una práctica normal durante la generación de PDF, XPS e imágenes y garantiza que el documento o imagen convertidos aparezcan idénticos para cualquier espectador.

{{% /alert %}}

## **Acerca de las fuentes**

### **Disponibilidad y sustitución de fuentes**

Una hoja de cálculo puede estar formateada con diversas fuentes como Arial, Times New Roman, Verdana y otras. Cuando Aspose.Cells renderiza una hoja de cálculo, intenta seleccionar las fuentes que se utilizan en la hoja de cálculo. Sin embargo, hay situaciones en las que la fuente exacta puede no estar disponible, por lo que Aspose.Cells debe sustituir una fuente similar en su lugar.

A continuación se muestra el proceso que Aspose.Cells sigue detrás de escena.

1. Aspose.Cells intenta encontrar las fuentes en el sistema de archivos que coincidan con el nombre exacto de la fuente utilizada en la hoja de cálculo.
2. Si Aspose.Cells no puede encontrar fuentes con el mismo nombre exacto, intenta usar la fuente predeterminada especificada bajo la propiedad DefaultStyle.Font del libro de trabajo.
3. Si Aspose.Cells no puede localizar la fuente definida bajo la propiedad DefaultStyle.Font del libro de trabajo, intenta seleccionar las fuentes más adecuadas de entre todas las fuentes disponibles.
1. Finalmente, si Aspose.Cells no puede encontrar ninguna fuente en el sistema de archivos, renderiza la hoja de cálculo usando Arial.

### **Dónde busca Aspose.Cells las fuentes**

Aspose.Cells intenta encontrar fuentes TrueType en el sistema de archivos automáticamente. La mayoría de las veces puedes confiar en el comportamiento predeterminado de Aspose.Cells para encontrar fuentes TrueType, pero a veces puede ser necesario especificar carpetas que contengan las fuentes TrueType utilizando el método de fábrica FontConfigs.setFontFolder.

### **Problemas y soluciones típicos relacionados con las fuentes**

Esta tabla enumera algunos de los problemas que podrías encontrar al renderizar hojas de cálculo a PDF usando Aspose.Cells y sus soluciones.

{{% alert color="primary" %}}

Ten en cuenta que al copiar fuentes, la mayoría están protegidas por derechos de autor. Localiza previamente la licencia de una fuente y verifica que se puedan transferir libremente a otra máquina. 

{{% /alert %}}

|**Problema** |**Motivo** |**Solución** |
| :- | :- | :- |
|El diseño y las fuentes en el documento renderizado son diferentes del original. |Estás usando Aspose.Cells en Linux o Mac OS donde las fuentes TrueType no están presentes por defecto, por lo que Aspose.Cells no puede localizar las fuentes en tu computadora. |Copia archivos de fuentes TrueType de una máquina con Windows o instala un paquete de fuentes TrueType. Utiliza el método de fábrica FontConfigs.setFontFolder para especificar la ubicación de los archivos de fuentes.|

{{% alert color="primary" %}}

Consulta los artículos detallados en

- [Cómo colocar fuentes TrueType en Linux](/cells/es/java/how-to-install-truetype-fonts-on-linux/).
- [Cómo especificar la ubicación de fuentes TrueType](/cells/es/java/how-to-specify-truetype-fonts-location/).
- [Cómo obtener advertencias cuando ocurre una sustitución de fuentes](/cells/es/java/get-warnings-for-font-substitution-while-rendering-excel-file/)

{{% /alert %}}
