---
title: Détecter le type d hyperlien
type: docs
weight: 160
url: /fr/nodejs-cpp/detect-hyperlink-type/
description: Apprenez comment détecter le type d hyperlien via l API Aspose.Cells for Node.js via C++.
keywords: Détecter le type d hyperlien avec Node.js via C++, Détecter le type d hyperlien avec Node.js via C++, Obtenir le type d hyperlien avec Node.js via C++
---

## **Détecter le type de lien hypertexte**

Un fichier Excel peut avoir différents types d'hyperliens comme externe, référence de cellule, chemin de fichier, etc. Aspose.Cells for Node.js via C++ supporte la détection du type d'hyperlien. Les types d'hyperliens sont représentés par l'énumération [**TargetModeType**](https://reference.aspose.com/cells/nodejs-cpp/targetmodetype). L'énumération [**TargetModeType**](https://reference.aspose.com/cells/nodejs-cpp/targetmodetype) comporte les membres suivants.

- Externe : lien externe
- CheminFichier : Chemin local et complet vers des fichiers/dossiers.
- Email : Email
- RéférenceDeCellule : Lien vers une cellule ou plage nommée.

Pour vérifier le type d'hyperlien, la classe [**Hyperlink**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink) fournit une méthode [**getLinkType()**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink/#getLinkType--) avec un type de retour [**TargetModeType**](https://reference.aspose.com/cells/nodejs-cpp/targetmodetype). Le code suivant démontre l'utilisation de la méthode [**getLinkType()**](https://reference.aspose.com/cells/nodejs-cpp/hyperlink/#getLinkType--) en utilisant ce [fichier Excel source](94896195.xlsx).

### Code source

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Hyperlinks-DetectHyperlinkType.js" >}}


Ce qui suit est le résultat généré par le code donné ci-dessus.

### Sortie de la Console
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
{{< app/cells/assistant language="nodejs-cpp" >}}
