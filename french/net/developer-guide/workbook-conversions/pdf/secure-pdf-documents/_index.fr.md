---
title: Documents PDF sécurisés
type: docs
weight: 120
url: /fr/net/secure-pdf-documents/
---
{{% alert color="primary" %}}

Parfois, les développeurs doivent travailler avec des fichiers PDF cryptés. Par exemple, ils doivent sécuriser les documents avec des mots de passe d'utilisateur et de propriétaire afin que n'importe qui ne puisse pas les ouvrir, ou souhaitent restreindre l'impression ou l'extraction du contenu du document.

Cet article explique comment transmettre les options de sécurité PDF lors de l'enregistrement de feuilles de calcul au format PDF.

{{% /alert %}}

 Aspose.Cells fournit le[**Aspose.Cells.Rendering.PdfSecurity**](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity) espace de noms pour travailler avec la sécurité. L'exemple de code ci-dessous décrit comment sécuriser des PDF avec Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SecurePDFDocuments-1.cs" >}}

{{% alert color="primary" %}}

 Si la feuille de calcul contient des formules, il est préférable d'appeler[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)juste avant de le rendre au format PDF. Cela garantit que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
