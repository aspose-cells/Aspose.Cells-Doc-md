---
title: Documents sécurisés PDF
type: docs
weight: 120
url: /fr/python-net/secure-pdf-documents/
description: Découvrez comment transmettre les options de sécurité PDF lors de l'enregistrement de feuilles de calcul dans PDF avec Aspose.Cells for Python via .NET API.
keywords: Python write security options to pdf, encrypt PDF document 
---
{{% alert color="primary" %}}

Parfois, les développeurs doivent travailler avec des fichiers PDF cryptés. Par exemple:

- Sécurisez les documents avec les mots de passe du propriétaire et de l'utilisateur afin que n'importe qui puisse les ouvrir.
- Définissez des restrictions ou des autorisations sur le document après son ouverture. par exemple, restreindre si le contenu du document peut être imprimé ou extrait.

Cet article explique comment transmettre les options de sécurité PDF lors de l'enregistrement de feuilles de calcul dans PDF.

{{% /alert %}}

 Aspose.Cells for Python via .NET fournit[**Options de sécurité Pdf**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/)pour travailler avec la sécurité. Vous pouvez définir des mots de passe propriétaire et utilisateur lors de l'enregistrement sous PDF. Le mot de passe propriétaire ou le mot de passe utilisateur sera requis pour ouvrir le document crypté PDF et le consulter.

- Le mot de passe de l'utilisateur peut être nul ou une chaîne vide, dans ce cas aucun mot de passe ne sera demandé à l'utilisateur lors de l'ouverture du document PDF.
- L'ouverture du document PDF avec le mot de passe propriétaire correct permet un accès complet (sans aucune restriction d'accès spécifiée) au document.
- L'ouverture du document PDF avec le mot de passe utilisateur correct (ou l'ouverture d'un document qui n'a pas de mot de passe utilisateur) permet un accès limité selon les autorisations spécifiées.

L'exemple de code ci-dessous décrit comment sécuriser les PDF avec Aspose.Cells for Python via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-Articles-SecurePDFDocuments-1.py" >}}

{{% alert color="primary" %}}

 Si la feuille de calcul contient des formules, il est préférable d'appeler[**Classeur.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) juste avant de le restituer en PDF. Cela garantit que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
