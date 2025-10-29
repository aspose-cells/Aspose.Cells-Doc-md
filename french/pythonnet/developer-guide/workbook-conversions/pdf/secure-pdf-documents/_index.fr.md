---
title: Documents PDF sécurisés
type: docs
weight: 120
url: /fr/python-net/secure-pdf-documents/
description: Apprenez comment passer des options de sécurité PDF lors de l enregistrement de feuilles de calcul en PDF avec l API Aspose.Cells pour Python via .NET.
keywords: Écrire des options de sécurité en Python au format PDF, chiffrer un document PDF 
---

{{% alert color="primary" %}}

Parfois, les développeurs ont besoin de travailler avec des fichiers PDF cryptés. Par exemple :

- Sécuriser les documents avec des mots de passe propriétaire et utilisateur afin que n'importe qui ne puisse pas l'ouvrir.
- Définir des restrictions ou des autorisations sur le document après l'ouverture du document. par exemple, restreindre si le contenu du document peut être imprimé ou extrait.

Cet article explique comment passer des options de sécurité PDF lors de l'enregistrement des feuilles de calcul au format PDF.

{{% /alert %}}

Aspose.Cells pour Python via .NET offre [**PdfSecurityOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/) pour travailler avec la sécurité. Vous pouvez définir des mots de passe propriétaire et utilisateur lors de l'enregistrement au format PDF. Le mot de passe propriétaire ou utilisateur sera requis pour ouvrir le document PDF crypté en vue.

- Le mot de passe utilisateur peut être nul ou une chaîne vide, dans ce cas aucun mot de passe ne sera requis de la part de l'utilisateur lors de l'ouverture du document PDF.
- Ouvrir le document PDF avec le bon mot de passe propriétaire permet un accès complet (sans aucune restriction d'accès spécifiée) au document.
- Ouvrir le document PDF avec le bon mot de passe utilisateur (ou ouvrir un document qui n'a pas de mot de passe utilisateur) permet un accès limité comme les autorisations spécifiées.

Le code d'exemple ci-dessous décrit comment sécuriser les PDF avec Aspose.Cells pour Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-Articles-SecurePDFDocuments-1.py" >}}

{{% alert color="primary" %}}

Si le classeur contient des formules, il est préférable d'appeler [**Workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) juste avant de le rendre au format PDF. Cela garantit que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
