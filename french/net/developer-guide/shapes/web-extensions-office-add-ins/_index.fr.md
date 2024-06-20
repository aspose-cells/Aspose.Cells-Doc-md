---
title: Extensions Web  Modules complémentaires Office
type: docs
weight: 130
url: /fr/net/web-extensions-office-add-ins/
---

Les extensions Web étendent les applications Office et interagissent avec le contenu des documents Office. Les extensions Web ajoutent des fonctionnalités supplémentaires au client Office pour améliorer l'expérience utilisateur et la productivité.

Aspose.Cells offre également la possibilité de travailler avec des extensions Web.

## **Ajouter une extension Web**

Vous pouvez ajouter des extensions Web (compléments Office) dans Excel en cliquant sur l'onglet **Insérer** puis en cliquant sur le lien **Magasin**/**Obtenir des compléments**. Dans la boîte de dialogue des compléments, recherchez le complément souhaité et ajoutez-le.

Aspose.Cells propose également la fonctionnalité d'ajouter des extensions Web en utilisant les classes [**WebExtension**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextension) et [**WebExtensionTaskPane**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextensiontaskpane). L'exemple de code suivant démontre l'utilisation des classes [**WebExtension**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextension) et [**WebExtensionTaskPane**](https://reference.aspose.com/cells/net/aspose.cells.webextensions/webextensiontaskpane) pour ajouter une extension web au fichier Excel. Veuillez consulter le [fichier Excel de sortie](89849869.xlsx) généré par le code pour référence.

### **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AddWebExtension-1.cs" >}}

## **Accéder aux informations sur l'extension Web**

Aspose.Cells permet d'accéder aux informations des extensions Web dans un fichier Excel. L'exemple de code suivant montre comment accéder aux informations d'extension Web en chargeant le [fichier Excel d'exemple](89849870.xlsx). Veuillez consulter la sortie de la console générée par le code pour référence.

### **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AccessWebExtensionInformation-1.cs" >}}

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
