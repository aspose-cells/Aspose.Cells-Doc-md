---
title: Public API Changements dans Aspose.Cells 17.1.0
type: docs
weight: 20
url: /fr/cpp/public-api-changes-in-aspose-cells-17-1-0/
---
{{% alert color="primary" %}} 

Ce document décrit les modifications apportées au Aspose.Cells API de la version 16.12.0 à 17.1.0 qui peuvent intéresser les développeurs de modules/applications. Il inclut non seulement les méthodes publiques nouvelles et mises à jour, les classes ajoutées et supprimées, etc., mais également une description de tout changement de comportement dans les coulisses de Aspose.Cells.

{{% /alert %}} 
## **API ajoutées**
### **Prise en charge des plages nommées**
 Aspose.Cells pour C++ prend désormais en charge la création ainsi que la manipulation des plages nommées. L'extrait de code suivant montre à quel point il est simple d'utiliser Aspose.Cells pour C++ API pour[créer des plages nommées](/cells/fr/cpp/create-named-range-in-a-workbook/).

**C++**

{{< highlight "csharp" >}}

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

 Outre la création de nouvelles plages nommées, les API Aspose.Cells pour C++ prennent également en charge la manipulation des plages nommées existantes. L'extrait de code suivant utilise le Aspose.Cells pour C++ API pour[manipuler une plage nommée existante](/cells/fr/cpp/manipulate-named-range-in-a-workbook/).

**C++**

{{< highlight "csharp" >}}

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
### **Ajout de la méthode ICells :: LinkToXmlMap**
La méthode LinkToXmlMap a été ajoutée à la classe ICells qui est utile pour lier une carte XML.
### **Ajout de la méthode ICells :: ImportCSV**
La méthode ImportCSV a été ajoutée à la classe ICells, ce qui est utile pour importer un fichier CSV dans les cellules d'une feuille de calcul.
### **Méthode ICells ::ImportTwoDimensionArray ajoutée**
La méthode GetIProtectedRangeCollection a été ajoutée à la classe ICells, ce qui est utile pour importer un tableau de données à deux dimensions dans une feuille de calcul.
### **Ajout de la méthode IWorksheet :: GetIProtectedRangeCollection**
La méthode GetIProtectedRangeCollection a été ajoutée à la classe IWorksheet qui est utile pour récupérer la collection d'objets IProtectedRange.
### **Ajout de la méthode IWorksheet :: GetIProtectedRangeCollection**
La méthode GetIProtectedRangeCollection a été ajoutée à la classe IWorksheet, ce qui est utile pour récupérer la collection de plages d'édition à partir de la feuille de calcul.
### **Ajout de la méthode IWorkbookSettings :: ClearPivottables**
La méthode ClearPivottables a été ajoutée à la classe IWorkbookSettings, ce qui est utile pour effacer tous les tableaux croisés dynamiques d'une feuille de calcul donnée.
### **Ajout de la méthode IWorksheetCollection :: CreateIRange**
La méthode CreateIRange a été ajoutée à la classe IWorksheetCollection, ce qui est utile pour créer un objet de l'IRange en transmettant des références de cellule au format chaîne.
### **Ajout de la méthode IExternalLink :: IsVisible**
La méthode IsVisible obtient le statut de visibilité d'un lien externe dans l'application Excel.
### **Ajout des méthodes GetScaleCrop et SetScaleCrop**
Aspose.Cells pour C++ 17.1.0 a exposé les méthodes GetScaleCrop & SetScaleCrop à la classe IBuiltInDocumentPropertyCollection. Ces méthodes sont utiles pour obtenir ou définir la propriété ScaleCrop qui indique le mode d'affichage de la vignette du document.
### **Ajout des méthodes GetLinksUpToDate et SetLinksUpToDate**
Aspose.Cells pour C++ 17.1.0 a exposé les méthodes GetLinksUpToDate & SetLinksUpToDate à la classe IBuiltInDocumentPropertyCollection. Ces méthodes sont utiles pour obtenir ou définir la propriété LinkUpToDate qui indique si les liens hypertexte d'un document sont à jour.
### **Ajout des méthodes GetAbsolutePath et SetAbsolutePath**
Aspose.Cells pour C++ 17.1.0 a exposé les méthodes GetAbsolutePath & SetAbsolutePath à la classe IWorkbook. Ces méthodes sont utiles pour obtenir ou définir le chemin absolu du fichier qui ne peut être utilisé que pour les liens externes.
### **Ajout des méthodes GetFormula et SetFormula**
Cette version de Aspose.Cells pour C++ a exposé les méthodes GetFormula et SetFormula pour la classe IListColumn. Ces méthodes sont utiles pour obtenir ou définir la formule d'une colonne de liste.
### **Ajout des méthodes GetCheckCompatibility et SetCheckCompatibility**
Cette version de Aspose.Cells pour C++ a exposé les méthodes GetCheckCompatibility et GetCheckCompatibility pour la classe IWorkbookSettings. Ces méthodes sont utiles pour obtenir ou définir la propriété de vérification de compatibilité indiquant si le API doit vérifier la compatibilité lors de l'enregistrement du classeur. La valeur par défaut est true et peut être définie sur false si l'exigence de l'application n'est pas de vérifier la compatibilité.
### **Ajout des méthodes GetILightCellsDataHandler et SetILightCellsDataHandler**
Aspose.Cells pour C++ a maintenant exposé les méthodes GetILightCellsDataHandler & SetILightCellsDataHandler pour la classe ILoadOptions. Ces méthodes désignent le gestionnaire de données pour le traitement des données des cellules lors de la lecture du fichier de modèle.
### **Ajout des méthodes GetCultureInfo et SetCultureInfo**
Aspose.Cells pour C++ a exposé les méthodes GetCultureInfo & SetCultureInfo pour la classe ILoadOptions. Ces méthodes peuvent obtenir ou définir les informations de culture système au moment du chargement du fichier.
## **API supprimées**
### **Suppression de la méthode ICells :: MaxDataRowInColumn**
Il est conseillé d'utiliser la méthode ICells::GetLastDataRow à la place.
### **Suppression de la méthode ICell :: GetConditionalIStyle**
Il est conseillé d'utiliser la méthode ICell::GetIConditionalFormattingResult à la place.
### **Suppression des méthodes IPageSetup :: GetDraft et SetDraft**
Il est conseillé d'utiliser à la place les méthodes IPageSetup::GetPrintDraft & IPageSetup::SetPrintDraft.

{{% alert color="primary" %}} 

Avec la sortie de Aspose.Cells pour C++ 17.1.0, nous avons supprimé quelques méthodes qui n'étaient pas utilisées donc jugées inutiles. Voici la liste de toutes ces méthodes.

- IPaneCollection :: Méthodes GetAcitvePaneType & SetAcitvePaneType
- IRange::Méthode ToString
- IRow::Méthode Equals
- Méthode IWorkbook::SetISettings
- Méthode ICell::ToString()
- Méthode ICell::Equals(ObjectPtr)
- Méthode ICell :: GetHashCode
- IWorksheet::Méthode ToString

{{% /alert %}}
