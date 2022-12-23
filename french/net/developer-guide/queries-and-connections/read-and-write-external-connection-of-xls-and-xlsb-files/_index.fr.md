---
title: Lire et écrire la connexion externe des fichiers XLS et XLSB
type: docs
weight: 80
url: /fr/net/read-and-write-external-connection-of-xls-and-xlsb-files/
---
## **Scénarios d'utilisation possibles**

Aspose.Cells prend déjà en charge la connexion externe en lecture et en écriture du fichier XLSX mais maintenant, il prend également en charge cette fonctionnalité pour les fichiers XLSB et XLS. Cependant, le code est le même pour tous les types de formats.

## **Lire et écrire la connexion externe du fichier XLS/XLSB**

 L'exemple de code suivant charge l'exemple de fichier XLSB (XLS peut également être chargé) et lit sa première connexion externe qui est en fait une connexion Access DB Microsoft. Il modifie alors le[**DBConnection.Name**](https://reference.aspose.com/cells/net/aspose.cells.externalconnections/externalconnection/properties/name) propriété et l'enregistre en tant que fichier de sortie XLS/XLSB. La capture d'écran montre l'effet du code sur[exemple de fichier XLSB](51740722.xlsb) et[fichier de sortie XLSB](51740723.xlsb) après son exécution. Veuillez également consulter la sortie de la console de l'exemple de code ci-dessous pour référence.

![tâche : image_autre_texte](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)

## **Exemple de code**

Le code suivant fonctionnera pour les fichiers XLSB et XLS en chargeant et en enregistrant les fichiers avec l'extension appropriée.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ReadAndWriteExternalConnectionOfXLSBFile.cs" >}}

## **Sortie console**

{{< highlight "java" >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}
