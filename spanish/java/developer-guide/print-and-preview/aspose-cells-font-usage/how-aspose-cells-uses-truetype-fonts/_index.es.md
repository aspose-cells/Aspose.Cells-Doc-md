---
title: Cómo Aspose.Cells utiliza fuentes TrueType
type: docs
weight: 10
url: /es/java/how-aspose-cells-uses-truetype-fonts/
---
{{% alert color="primary" %}}

Aspose.Cells requiere fuentes TrueType al representar hojas de cálculo en formatos como PDF, XPS e imágenes.

Cuando Aspose.Cells representa una hoja de cálculo, requiere acceso a las fuentes TrueType utilizadas en la hoja de cálculo. Esta es una práctica normal durante PDF, XPS y la generación de imágenes y garantiza que el documento o la imagen convertidos parezcan idénticos para cualquier espectador.

{{% /alert %}}

## **Acerca de las fuentes**

### **Disponibilidad y sustitución de fuentes**

Una hoja de cálculo se puede formatear usando varias fuentes como Arial, Times New Roman, Verdana y otras. Cuando Aspose.Cells representa una hoja de cálculo, intenta seleccionar las fuentes que se utilizan en la hoja de cálculo. Sin embargo, hay situaciones en las que la fuente exacta puede no estar disponible, por lo que Aspose.Cells tiene que sustituirla por una fuente similar.

A continuación se muestra el proceso que Aspose.Cells sigue detrás de escena.

1. Aspose.Cells intenta encontrar las fuentes en el sistema de archivos que coincidan con el nombre de fuente exacto utilizado en la hoja de cálculo.
1. Si Aspose.Cells no puede encontrar fuentes con exactamente el mismo nombre, intenta usar la fuente predeterminada especificada en la propiedad DefaultStyle.Font del libro de trabajo.
1. Si Aspose.Cells no puede ubicar la fuente definida en la propiedad DefaultStyle.Font del libro de trabajo, intenta seleccionar las fuentes más adecuadas de todas las fuentes disponibles.
1. Finalmente, si Aspose.Cells no puede encontrar ninguna fuente en el sistema de archivos, procesa la hoja de cálculo usando Arial.

### **Donde Aspose.Cells busca fuentes**

Aspose.Cells intenta encontrar fuentes TrueType en el sistema de archivos automáticamente. La mayoría de las veces puede confiar en el comportamiento predeterminado de Aspose.Cell para encontrar fuentes TrueType, pero a veces puede necesitar especificar carpetas que contengan las fuentes TrueType utilizando el método de fábrica FontConfigs.setFontFolder.

### **Problemas típicos relacionados con fuentes y soluciones**

Esta tabla enumera algunos de los problemas que puede encontrar al procesar hojas de cálculo en PDF usando Aspose.Cells y sus soluciones.

{{% alert color="primary" %}}

 Cuando copie cualquier fuente, tenga en cuenta que la mayoría de las fuentes tienen derechos de autor. Primero ubique la licencia de una fuente de antemano y verifique que se puedan transferir libremente a otra máquina.

{{% /alert %}}

|**Problema** |**Razón** |**Solución** |
|:- |:- |:- |
| El diseño y las fuentes del documento renderizado son diferentes del original.| Está utilizando Aspose.Cells en Linux o Mac OS donde las fuentes TureType no están presentes de forma predeterminada, por lo que Aspose.Cells no puede ubicar las fuentes en su computadora.|Copie archivos de fuentes TrueType desde una máquina Windows o instale un paquete de fuentes TrueType. Utilice el método de fábrica FontConfigs.setFontFolder para especificar la ubicación de los archivos de fuentes.|

{{% alert color="primary" %}}

Consulte los artículos detallados sobre

- [Cómo colocar fuentes TrueType en Linux](/cells/es/java/how-to-install-truetype-fonts-on-linux/).
- [Cómo especificar la ubicación de las fuentes TrueType](/cells/es/java/how-to-specify-truetype-fonts-location/).
- [Cómo recibir advertencias cuando se produce la sustitución de fuentes](/cells/es/java/get-warnings-for-font-substitution-while-rendering-excel-file/)

{{% /alert %}}
