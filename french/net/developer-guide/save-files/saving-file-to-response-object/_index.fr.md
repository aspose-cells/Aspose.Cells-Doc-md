---
title: Enregistrement du fichier dans l'objet de réponse
type: docs
weight: 50
url: /fr/net/saving-file-to-response-object/
---
{{% alert color="primary" %}}

Aspose.Cells permet de manipuler des fichiers. Cet article explique les différentes façons dont les fichiers peuvent être enregistrés dans un objet de réponse.

{{% /alert %}}

## **Enregistrement du fichier dans l'objet de réponse**

 Il est également possible de générer dynamiquement un fichier et de l'envoyer directement à un navigateur client. Pour ce faire, utilisez une version spéciale surchargée du**[Enregistrer] (https://reference.aspose.com/cells/net/aspose.cells.workbook/save/methods/5)**méthode qui accepte les paramètres suivants :

-  ASP.NET**[HttpResponse](https://docs.microsoft.com/en-gb/dotnet/api/system.web.httpresponse?view=netframework-4.8)**objet.
- Nom de fichier.
- **[ContentDisposition](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition)**, le type de disposition de contenu du fichier de sortie.
- **[Options de sauvegarde] (https://reference.aspose.com/cells/net/aspose.cells/saveoptions)**, le type de format de fichier

 Le**[ContentDisposition](https://reference.aspose.com/cells/net/aspose.cells/contentdisposition)**L'énumération détermine si le fichier envoyé au navigateur offre la possibilité de s'ouvrir seul directement dans le navigateur ou dans une application associée à .xls/.xlsx ou à une autre extension.

L'énumération contient les types de sauvegarde prédéfinis suivants :

|**Taper**|**Description**|
|:- |:- |
|Attachement|Envoie la feuille de calcul au navigateur et s'ouvre dans une application en tant que pièce jointe associée à .xls/.xlsx ou à d'autres extensions|
|En ligne|Envoie le document au navigateur et présente une option pour enregistrer la feuille de calcul sur le disque ou l'ouvrir dans le navigateur|

### **XLS Fichiers**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSFile-1.cs" >}}

### **XLSX Fichiers**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveXLSXFile-1.cs" >}}

### **PDF Fichiers**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SaveInPdfFormat-1.cs" >}}

### **Noter**

En raison de l'objet "System.Web.HttpResponse" ne contenu pas dans .NET5 et .Netstandard,
Donc, cette fonction n'existe pas dans les versions Aspose.Cells .NET5 et .Netstandard, vous pouvez vous référer au code suivant pour enregistrer le fichier dans le flux, puis effectuer l'opération dans le flux.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-SavingFiletoStream-1.cs" >}}

