---
title: Cambiar la fuente solo de los caracteres Unicode específicos al guardar en PDF
type: docs
weight: 260
url: /es/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---

{{% alert color="primary" %}} 

Algunos caracteres Unicode no pueden ser mostrados por la fuente especificada por el usuario. Uno de estos caracteres Unicode es **Guión no separable** (U+2011) y su número Unicode es 8209. Este carácter no puede ser mostrado con **Times New Roman**, pero puede ser mostrado con otras fuentes como **Arial Unicode MS**.

Cuando un carácter de este tipo ocurre dentro de alguna palabra u oración que está en una fuente específica como Times New Roman, entonces Aspose.Cells cambia la fuente de la palabra u oración completa a una fuente que puede mostrar este carácter como Arial Unicode MS.

Sin embargo, este comportamiento es indeseable para algunos usuarios y desean que solo se cambie la fuente del carácter específico en lugar de cambiar la fuente de toda la palabra u oración.

Para abordar este problema, Aspose.Cells proporciona la propiedad PdfSaveOptions.IsFontSubstitutionCharGranularity que debe configurarse en true para que solo la fuente del carácter específico que no se puede mostrar sea cambiada a una fuente que se pueda mostrar y el resto de la palabra u oración permanezca en la fuente original.

{{% /alert %}} 
## **Ejemplo**
La siguiente captura de pantalla compara los dos PDF generados por el código de muestra a continuación.

Uno se generó sin configurar la propiedad PdfSaveOptions.IsFontSubstitutionCharGranularity y el otro se generó después de configurar la propiedad PdfSaveOptions.IsFontSubstitutionCharGranularity en true.

Como se puede ver en el primer PDF, la fuente de toda la oración ha cambiado de Times New Roman a Arial Unicode MS debido al Guión no separable. Mientras que en el segundo PDF, solo la fuente del Guión no separable ha cambiado.

|**Primer archivo PDF**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**Segundo archivo PDF**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **Código de muestra**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ChangeFontUnicodeCharacterToPdf-ChangeFontUnicodeCharacterWhileSavingToPdf.cs" >}}



{{< app/cells/assistant language="csharp" >}}
