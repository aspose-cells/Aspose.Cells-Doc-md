---
title: Cambie la fuente solo en los caracteres Unicode específicos mientras guarda en PDF
type: docs
weight: 260
url: /es/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
---
{{% alert color="primary" %}} 

 Algunos caracteres Unicode no se pueden mostrar con la fuente especificada por el usuario. Uno de esos caracteres Unicode es**Guión de no separación** (U+2011) y su número Unicode es 8209. Este carácter no se puede mostrar con**Times New Roman** , pero se puede mostrar con otras fuentes como**Arial Unicode MS**.

Cuando un carácter de este tipo aparece dentro de una palabra u oración que está en una fuente específica como Times New Roman, entonces Aspose.Cells cambia la fuente de la palabra u oración completa a una fuente que podría mostrar este carácter como Arial Unicode a MS.

Sin embargo, este es un comportamiento indeseable para algunos usuarios y quieren que solo se cambie la fuente de ese carácter específico en lugar de cambiar la fuente de la palabra u oración completa.

Para solucionar este problema, Aspose.Cells proporciona la propiedad PdfSaveOptions.IsFontSubstitutionCharGranularity que debe establecerse como verdadera para que solo la fuente del carácter específico que no se puede mostrar se cambie a una fuente que se pueda mostrar y el resto de la palabra u oración debe permanecer en la fuente original.

{{% /alert %}} 
## **Ejemplo**
La siguiente captura de pantalla compara los dos PDF de salida generados por el código de muestra a continuación.

Uno se genera sin establecer la propiedad PdfSaveOptions.IsFontSubstitutionCharGranularity y el otro se generó después de establecer la propiedad PdfSaveOptions.IsFontSubstitutionCharGranularity en verdadero.

Como puede ver en el primer PDF, la fuente de la oración completa ha cambiado de Times New Roman a Arial Unicode MS debido a Non-Breaking Hyphen. Mientras que en el segundo PDF, solo ha cambiado la fuente de Non-Breaking Hyphen.

|**Primer archivo PDF**|
|:- |
|![todo:imagen_alternativa_texto](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**Segundo archivo PDF**|
|:- |
|![todo:imagen_alternativa_texto](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **Código de muestra**


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-ChangeFontUnicodeCharacterToPdf-ChangeFontUnicodeCharacterWhileSavingToPdf.cs" >}}



