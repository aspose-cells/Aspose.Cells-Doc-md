---
title: Aspose.Cells for .NET 20.10 Notes de mise à jour
type: docs
weight: 7
url: /fr/net/aspose-cells-for-net-20-10-release-notes/
---
{{% alert color="primary" %}}

 Cette page contient des notes de version pour[Aspose.Cells for .NET 20.10](https://www.nuget.org/packages/Aspose.Cells/20.10.0).

{{% /alert %}}

|**Clé**|**Sommaire**|**Catégorie**|
|:- |:- |:- |
|CELLSNET-47625|Vérifie le mot de passe pour les fichiers cryptés|Nouvelle fonctionnalité|
|CELLSNET-47601|Rendre des lignes et des colonnes supplémentaires en HTML sans perturber les formules/références pour ressembler à la sortie avec MS Excel|Nouvelle fonctionnalité|
|CELLSNET-47619|Aspose Problème de ChartSetChartDataRange|Renforcement|
|CELLSNET-47632|Différence de structure et d'ordre dans OLE de l'entrée et de la sortie après l'enregistrement du fichier|Renforcement|
|CELLSNET-47644|Différentes connexions externes récupérées par rapport à MS Excel|Renforcement|
|CELLSNET-47652|Problèmes d'espacement des polices lors de la définition du format des caractères|Renforcement|
|CELLSNET-47623|Opération de sauvegarde lente avec beaucoup de formules dans le fichier|Performance|
|CELLSNET-47606|L'application se bloque lors de la conversion d'Excel en PDF|Performance|
|CELLSNET-47611|Problème de calcul de la formule IRR|Punaise|
|CELLSNET-47616|Supprimer la plage se comportant différemment entre v20.8 et v20.9|Punaise|
|CELLSNETCORE-83|Le fichier Excel ne s'affichait pas correctement dans GridWeb|Punaise|
|CELLSNETCORE-86|Problème d'affichage de forme dans GridWeb|Punaise|
|CELLSNET-47597|Les zones de remplissage sont très différentes par rapport au fichier source|Punaise|
|CELLSNET-47614|Certains symboles manquent dans le PDF de sortie dans le rendu Excel vers PDF|Punaise|
|CELLSNET-47636|Conversion Excel en PDF - Le résultat passe sur la page en orientation paysage|Punaise|
|CELLSNET-47637|Conversion d'un problème Excel en PDF avec Calibri Light|Punaise|
|CELLSNET-42982|La taille et la mise en page du graphique ont été modifiées après Workbook.Combine|Punaise|
|CELLSNET-47594|Option pour obtenir des informations PlotBy et OnAction similaires à MS Excel|Punaise|
|CELLSNET-47595|Le graphique n'a pas été conservé correctement dans le fichier Excel lors du chargement et de l'enregistrement|Punaise|
|CELLSNET-47599|AddControlRefrernce n'ajoute pas de référence à MS Forms 2.0|Punaise|
|CELLSNET-47600|Les noms de contrôle de formulaire et quelques autres propriétés sont différents par rapport à MS Excel|Punaise|
|CELLSNET-47613|LTR et RTL ne sont pas conservés après le chargement et l'enregistrement avec le fichier XLSB|Punaise|
|CELLSNET-47615|Le fichier PowerPoint intégré dans le fichier Excel ne peut pas être ouvert après l'enregistrement|Punaise|
|CELLSNET-47645|Message de réparation émis par MS Excel après le chargement et l'enregistrement de fichiers Excel avec Aspose.Cells|Punaise|
|CELLSNET-47647|Message de réparation émis par Excel lors de la conversion XLSB->XLSX->XLSB|Punaise|
|CELLSNET-47648|Le fichier XLSB est corrompu après la conversion (XLSB-> XLSX-XLSB)|Punaise|
|CELLSNET-47658|La taille de la police est arrondie lorsque nous avons spécifié le symbole décimal avec le paramètre Région|Punaise|
|CELLSNETCORE-81|L'option "Envelopper le texte" n'est pas conservée dans le fichier XLSB après le chargement et l'enregistrement|Punaise|
|CELLSNETCORE-82|La feuille spécifique à l'intérieur du fichier XLSB se casse après le chargement et l'enregistrement|Punaise|
|CELLSNETCORE-84|Informations de style renvoyées avec le texte de l'en-tête|Punaise|
|CELLSNETCORE-85|Cells.InsertCutCells corrompt les notes|Punaise|
|CELLSNET-47544|Des images sont manquantes et la position du texte était incorrecte lors du rendu d'Excel sous Linux|Punaise|
|CELLSNET-47571|La conversion HTML à partir de XLS entre dans une boucle de conversion continue|Punaise|
|CELLSNET-47583|PivotTable.TableRange2 donne une mauvaise valeur pour le tableau croisé dynamique|Punaise|
|CELLSNET-47584|Aspose.Cells La conversion HTML vers Excel n'affichait pas d'images|Punaise|
|CELLSNET-47609|Diagram n'est pas affiché en html lorsque la feuille n'a pas d'autre contenu|Punaise|
|CELLSNET-47633|Le tableau croisé dynamique avec des dates ne se met pas à jour correctement|Punaise|
|CELLSNET-47635|Un trancheur sur une table différente génère un fichier corrompu|Punaise|
|CELLSNET-47620|Forme à l'erreur d'image lors de l'enregistrement au format PDF|Exception|
|CELLSNET-47608|NullReferenceException lors du chargement de XLSX|Exception|
|CELLSNET-47624|System.ArgumentException lors du chargement d'un fichier chiffré dans XLAM|Exception|
|CELLSNET-47630|L'argument spécifié était en dehors de la plage des valeurs valides exception lors de la suppression de la colonne|Exception|
|CELLSNET-47649|Une exception est déclenchée lors de la lecture de DBConnection.PowerQueryFormula à partir du fichier XLSX|Exception|
|CELLSNET-47655|CellsException lors de la conversion d'Excel en PDF|Exception|
|CELLSNETCORE-80|Impossible de caster l'exception d'objet lors de la conversion de XLSB en XLSM|Exception|
|CELLSNET-47593|Exception lors de la tentative d'ouverture d'un HTM particulier|Exception|
|CELLSNET-47656|Forme à l'image Erreur lors de la conversion de XLSB en PDF|Exception|

## **Public API et modifications incompatibles avec les versions antérieures**

Voici une liste de toutes les modifications apportées au public API, telles que les membres ajoutés, renommés, supprimés ou obsolètes, ainsi que toute modification non rétrocompatible apportée à Aspose.Cells for .NET. Si vous avez des inquiétudes concernant l'un des changements répertoriés, veuillez le signaler sur le forum d'assistance Aspose.Cells.

### **Ajoute l'énumération ExceptionType.Permission**

Représente ExceptionType.Permission.

### **Ajoute la propriété ExternalConnection.PowerQueryFormula.**

Obtient la définition de la formule de requête de puissance.

### **Ajoute la méthode FileFormatUtil.VerifyPassword.**

Vérifie si le mot de passe est valide pour le fichier.

### **Ajoute la méthode VbaProject.Copy().**

Copie le projet VBA.

### **Ajoute la propriété XlsSaveOptions.MatchColor.**

Indique si la couleur correspond si la couleur n'est pas dans la palette lors de l'enregistrement du fichier .xls.

### **Supprime la propriété Series.Line obsolète.**

Utilisez plutôt la propriété Series.Border.
