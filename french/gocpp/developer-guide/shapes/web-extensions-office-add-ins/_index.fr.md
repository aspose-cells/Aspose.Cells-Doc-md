---
title: Extensions Web  Compléments Office avec Golang via C++
linktitle: Extensions Web  Modules complémentaires Office
type: docs
weight: 130
url: /fr/go-cpp/web-extensions-office-add-ins/
description: Apprenez comment ajouter et accéder aux Extensions Web (Compléments Office) dans les fichiers Excel en utilisant Aspose.Cells avec Golang via C++.
---

Les extensions Web étendent les applications Office et interagissent avec le contenu des documents Office. Elles ajoutent des fonctionnalités supplémentaires aux clients Office pour améliorer l'expérience utilisateur et la productivité.

Aspose.Cells offre également la possibilité de travailler avec des extensions Web.

## **Ajouter une extension Web**

Vous pouvez ajouter des extensions Web (compléments Office) dans Excel en cliquant sur l'onglet **Insertion** puis en cliquant sur le lien **Store**/**Obtenir des compléments**. Dans la boîte de dialogue Add-ins, recherchez le complément souhaité et ajoutez-le.

Aspose.Cells offre également la fonctionnalité d'ajouter des extensions Web en utilisant les classes [**WebExtension**](https://reference.aspose.com/cells/go-cpp/webextension/) et [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/). L'exemple de code suivant montre comment utiliser les classes [**WebExtension**](https://reference.aspose.com/cells/go-cpp/webextension/) et [**WebExtensionTaskPane**](https://reference.aspose.com/cells/cpp/aspose.cells.webextensions/webextensiontaskpane/) pour ajouter une extension Web à un fichier Excel. Veuillez consulter le [fichier Excel de sortie](89849869.xlsx) généré par le code pour référence.

### **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WebExtensionsOfficeAddIns.go" >}}
## **Accéder aux informations sur l'extension Web**

Aspose.Cells permet d'accéder aux informations des extensions Web dans un fichier Excel. L'exemple de code ci-dessous montre comment accéder aux informations des extensions Web en chargeant le [fichier Excel d'exemple](89849870.xlsx). Veuillez consulter la sortie console générée par le code pour référence.

### **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WebExtensionsOfficeAddIns-1.go" >}}
### **Sortie console**

{{< highlight java >}}
Width: 350
IsVisible: True
IsLocked: False
DockState: right
StoreName: en-US
StoreType: OMEX
WebExtension.Id: 95D7ECE8-1355-492B-B6BF-27D25D0B0EEF
{{< /highlight >}}
