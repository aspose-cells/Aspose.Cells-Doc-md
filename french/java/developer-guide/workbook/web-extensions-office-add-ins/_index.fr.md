---
title: Extensions Web  Modules complémentaires Office
type: docs
weight: 120
url: /fr/java/web-extensions-office-add-ins/
---

Les extensions Web étendent les applications Office et interagissent avec le contenu des documents Office. Les extensions Web ajoutent des fonctionnalités supplémentaires au client Office pour améliorer l'expérience utilisateur et la productivité.

Aspose.Cells offre également la possibilité de travailler avec des extensions Web.

## **Ajouter une extension Web**

Vous pouvez ajouter des extensions Web (compléments Office) dans Excel en cliquant sur l'onglet **Insérer**, puis en cliquant sur le lien **Magasin**/**Obtenir des compléments**. Dans la boîte de dialogue Compléments, recherchez le complément souhaité et ajoutez-le.

Aspose.Cells propose également la fonctionnalité d'ajouter des extensions Web en utilisant les classes WebExtension et WebExtensionTaskPane. L'exemple de code suivant démontre l'utilisation des classes WebExtension et WebExtensionTaskPane pour ajouter une extension Web à un fichier Excel. Veuillez consulter le [fichier Excel de sortie](AddWebExtension_Out.xlsx) généré par le code pour référence.

### **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AddWebExtension-1.java" >}}

## **Accéder aux informations sur l'extension Web**

Aspose.Cells offre la possibilité d'accéder aux informations des extensions Web dans un fichier Excel. L'exemple de code suivant démontre comment accéder aux informations sur l'extension Web en chargeant le [fichier Excel d'exemple](WebExtensionsSample.xlsx). Veuillez consulter la sortie de la console générée par le code pour référence.

### **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AccessWebExtensionInformation-1.java" >}}

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
