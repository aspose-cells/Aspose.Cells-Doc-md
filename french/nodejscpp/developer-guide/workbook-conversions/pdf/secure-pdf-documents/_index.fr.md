---
title: Sécuriser les documents PDF avec Node.js via C++
linktitle: Documents PDF sécurisés
type: docs
weight: 120
url: /fr/nodejs-cpp/secure-pdf-documents/
description: Apprenez comment sécuriser des documents PDF en utilisant des mots de passe propriétaires et utilisateurs, et définir des permissions pour les fichiers PDF en utilisant Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Parfois, les développeurs ont besoin de travailler avec des fichiers PDF cryptés. Par exemple :

- Sécuriser les documents avec des mots de passe propriétaire et utilisateur afin que n'importe qui ne puisse pas l'ouvrir.
- Définir des restrictions ou des autorisations sur le document après l'ouverture du document. par exemple, restreindre si le contenu du document peut être imprimé ou extrait.

Cet article explique comment passer des options de sécurité PDF lors de l'enregistrement des feuilles de calcul au format PDF.

{{% /alert %}}

Aspose.Cells fournit [**PdfSecurityOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsecurityoptions/) pour travailler avec la sécurité. Vous pouvez définir des mots de passe propriétaire et utilisateur lors de l'enregistrement en PDF. Le mot de passe propriétaire ou utilisateur sera nécessaire pour ouvrir le PDF crypté pour la visualisation.

- Le mot de passe utilisateur peut être nul ou une chaîne vide ; dans ce cas, aucun mot de passe ne sera requis lors de l'ouverture du PDF.
- Ouvrir le document PDF avec le bon mot de passe propriétaire donne un accès complet (sans restrictions d'accès spécifiées) au document.
- Ouvrir le document PDF avec le bon mot de passe utilisateur (ou ouvrir un document qui n'a pas de mot de passe utilisateur) permet un accès limité comme les autorisations spécifiées.

Le code d'exemple ci-dessous décrit comment sécuriser des PDF avec Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const saveOption = new AsposeCells.PdfSaveOptions();
saveOption.setSecurityOptions(new AsposeCells.PdfSecurityOptions());

saveOption.getSecurityOptions().setUserPassword("user");
saveOption.getSecurityOptions().setOwnerPassword("owner");
saveOption.getSecurityOptions().setExtractContentPermission(false);
saveOption.getSecurityOptions().setPrintPermission(false);

workbook.save(path.join(dataDir, "securepdf_test.out.pdf"), saveOption);
```

{{% alert color="primary" %}}

Si le classeur contient des formules, il est préférable d'appeler [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) juste avant de le rendre au format PDF. Cela garantit que les valeurs dépendantes de la formule sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
