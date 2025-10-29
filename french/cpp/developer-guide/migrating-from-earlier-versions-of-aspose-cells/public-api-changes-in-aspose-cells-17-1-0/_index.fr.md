---
title: Changements de l API publique dans Aspose.Cells 17.1.0
type: docs
weight: 20
url: /fr/cpp/public-api-changes-in-aspose-cells-17-1-0/
---

{{% alert color="primary" %}} 

Ce document décrit les changements apportés à l'API Aspose.Cells de la version 16.12.0 à la version 17.1.0 qui pourraient intéresser les développeurs de modules/applications. Il inclut non seulement les nouvelles méthodes publiques et mises à jour, les classes ajoutées et supprimées, mais aussi une description de tout changement de comportement en coulisses dans Aspose.Cells.

{{% /alert %}} 
## **APIs ajoutées**
### **Support des Plages Nommées**
Aspose.Cells for C++ prend désormais en charge la création ainsi que la manipulation des Plages Nommées. L'extrait de code suivant démontre à quel point il est simple d'utiliser l'API Aspose.Cells for C++ pour [créer des plages nommées](/cells/fr/cpp/create-named-range-in-a-workbook/).

**C++**

{{< highlight csharp >}}

 //Path of your directory where you want to read or write files from

StringPtr dirPath = new String("D:\\Downloads\\");

//Path of output excel file

StringPtr outCreateNamedRange = (new String(dirPath))->Append(new String("outCreateNamedRange.xlsx"));

//Create a workbook

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook();

//Access first worksheet

intrusive_ptr<IWorksheet> ws = wb->GetIWorksheets()->GetObjectByIndex(0);

//Create a range

intrusive_ptr<IRange> rng = ws->GetICells()->CreateIRange((intrusive_ptr<String>)new String("A5:C10"));

//Set its name to make it named range

rng->SetName((intrusive_ptr<String>)new String("MyNamedRange"));

//Read the named range created above from names collection

intrusive_ptr<IName> nm = wb->GetIWorksheets()->GetINames()->GetObjectByIndex(0);

//Print its FullText and RefersTo properties

printf("Full Text: %s\n", nm->GetFullText()->charValue());

printf("Refers To: %s\n", nm->GetRefersTo()->charValue());

//Save the workbook in xlsx format

wb->Save(outCreateNamedRange, SaveFormat_Xlsx);

{{< /highlight >}}

En plus de créer de nouvelles Plages Nommées, les API Aspose.Cells for C++ prennent également en charge la manipulation des Plages Nommées existantes. L'extrait de code suivant utilise l'API Aspose.Cells for C++ pour [manipuler une plage nommée existante](/cells/fr/cpp/manipulate-named-range-in-a-workbook/).

**C++**

{{< highlight csharp >}}

 //Path of your directory where you want to read or write files from

StringPtr dirPath = new String("D:\\Downloads\\");

//Path of source excel file

StringPtr srcManipulateRange = (new String(dirPath))->Append(new String("srcManipulateRange.xlsx"));

//Path of output excel file

StringPtr outManipulateRange = (new String(dirPath))->Append(new String("outManipulateRange.xlsx"));

//Create a workbook

intrusive_ptr<IWorkbook> wb = Factory::CreateIWorkbook(srcManipulateRange);

//Read the named range created above from names collection

intrusive_ptr<IName> nm = wb->GetIWorksheets()->GetINames()->GetObjectByIndex(0);

//Print its FullText and RefersTo properties

printf("Full Text: %s\n", nm->GetFullText()->charValue());

printf("Refers To: %s\n", nm->GetRefersTo()->charValue());

//Manipulate the RefersTo property of NamedRange

nm->SetRefersTo((intrusive_ptr<String>)new String("=Sheet1!$D$5:$J$10"));

//Save the workbook in xlsx format

wb->Save(outManipulateRange, SaveFormat_Xlsx);

{{< /highlight >}}
### **Méthode ICells::LinkToXmlMap ajoutée**
La méthode LinkToXmlMap a été ajoutée à la classe ICells, ce qui est utile pour lier une carte XML.
### **Méthode ICells::ImportCSV ajoutée**
La méthode ImportCSV a été ajoutée à la classe ICells, ce qui est utile pour importer un fichier CSV dans les cellules d'une feuille de calcul.
### **Méthode ICells::ImportTwoDimensionArray ajoutée**
La méthode GetIProtectedRangeCollection a été ajoutée à la classe ICells, ce qui est utile pour importer un tableau de données bidimensionnel dans une feuille de calcul.
### **Méthode IWorksheet::GetIProtectedRangeCollection ajoutée**
La méthode GetIProtectedRangeCollection a été ajoutée à la classe IWorksheet, ce qui est utile pour récupérer la collection d'objets IProtectedRange.
### **Méthode IWorksheet::GetIProtectedRangeCollection ajoutée**
La méthode GetIProtectedRangeCollection a été ajoutée à la classe IWorksheet, ce qui est utile pour récupérer la collection de plages d'édition à partir de la feuille de calcul.
### **Méthode IWorkbookSettings::ClearPivottables ajoutée**
La méthode ClearPivottables a été ajoutée à la classe IWorkbookSettings, ce qui est utile pour effacer tous les tableaux croisés dynamiques d'une feuille de calcul donnée.
### **Ajout de la méthode IWorksheetCollection::CreateIRange**
La méthode CreateIRange a été ajoutée à la classe IWorksheetCollection, ce qui est utile pour créer un objet de type IRange en fournissant des références de cellules au format chaîne de caractères.
### **Ajout de la méthode IExternalLink::IsVisible**
La méthode IsVisible obtient le statut de visibilité d'un lien externe dans l'application Excel.
### **Ajout des méthodes GetScaleCrop & SetScaleCrop**
La version Aspose.Cells for C++ 17.1.0 a exposé les méthodes GetScaleCrop & SetScaleCrop à la classe IBuiltInDocumentPropertyCollection. Ces méthodes sont utiles pour obtenir ou définir la propriété ScaleCrop qui indique le mode d'affichage de la miniature du document.
### **Ajout des méthodes GetLinksUpToDate & SetLinksUpToDate**
La version Aspose.Cells for C++ 17.1.0 a exposé les méthodes GetLinksUpToDate & SetLinksUpToDate à la classe IBuiltInDocumentPropertyCollection. Ces méthodes sont utiles pour obtenir ou définir la propriété LinkUpToDate qui indique si les hyperliens dans un document sont à jour.
### **Ajout des méthodes GetAbsolutePath & SetAbsolutePath**
La version Aspose.Cells for C++ 17.1.0 a exposé les méthodes GetAbsolutePath & SetAbsolutePath à la classe IWorkbook. Ces méthodes sont utiles pour obtenir ou définir le chemin absolu du fichier qui ne peut être utilisé que pour les liens externes.
### **Ajout des méthodes GetFormula & SetFormula**
Cette version de Aspose.Cells for C++ a exposé les méthodes GetFormula & SetFormula pour la classe IListColumn. Ces méthodes sont utiles pour obtenir ou définir la formule d'une colonne de liste.
### **Ajout des méthodes GetCheckCompatibility & SetCheckCompatibility**
Cette version de Aspose.Cells for C++ a exposé les méthodes GetCheckCompatibility & GetCheckCompatibility pour la classe IWorkbookSettings. Ces méthodes sont utiles pour obtenir ou définir la propriété de vérification de compatibilité, indiquant si l'API doit vérifier la compatibilité lors de l'enregistrement du classeur. La valeur par défaut est true, et peut être définie sur false si les besoins de l'application ne nécessitent pas de vérifier la compatibilité.
### **Ajout des méthodes GetILightCellsDataHandler & SetILightCellsDataHandler**
Aspose.Cells for C++ a maintenant exposé les méthodes GetILightCellsDataHandler & SetILightCellsDataHandler pour la classe ILoadOptions. Ces méthodes désignent le gestionnaire de données pour le traitement des données de cellules lors de la lecture d'un fichier modèle.
### **Ajout des méthodes GetCultureInfo & SetCultureInfo**
Aspose.Cells for C++ a exposé les méthodes GetCultureInfo & SetCultureInfo pour la classe ILoadOptions. Ces méthodes peuvent obtenir ou définir les informations de culture système au moment du chargement du fichier.
## **APIs supprimées**
### **Méthode ICells::MaxDataRowInColumn supprimée**
Il est conseillé d'utiliser la méthode ICells::GetLastDataRow à la place.
### **Méthode ICell::GetConditionalIStyle supprimée**
Il est conseillé d'utiliser la méthode ICell::GetIConditionalFormattingResult à la place.
### **Méthodes IPageSetup::GetDraft & SetDraft supprimées**
Il est conseillé d'utiliser les méthodes IPageSetup::GetPrintDraft & IPageSetup::SetPrintDraft à la place.

{{% alert color="primary" %}} 

Avec la sortie de Aspose.Cells for C++ 17.1.0, nous avons supprimé quelques méthodes qui n'étaient pas utilisées et donc jugées inutiles. Voici la liste de toutes ces méthodes.

- Méthodes IPaneCollection::GetAcitvePaneType & SetAcitvePaneType
- Méthode IRange::ToString
- Méthode IRow::Equals
- Méthode IWorkbook::SetISettings
- Méthode ICell::ToString()
- Méthode ICell::Equals(ObjectPtr)
- Méthode ICell::GetHashCode
- Méthode IWorksheet::ToString

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
