---
title: Licence
type: docs
weight: 50
url: /fr/cpp/licensing/
---
## **Limites de la version d'évaluation**
 Une version d'évaluation gratuite de Aspose.Cells pour C++ peut être téléchargée à partir de la section des téléchargements du site Web de Aspose à :<https://downloads.aspose.com/cells/cpp>.
## **Appliquer la licence à l'aide d'un fichier ou d'un objet de flux**
La licence peut être chargée à partir d'un fichier ou d'un objet de flux. Aspose.Cells pour C++ essaiera de trouver la licence aux emplacements suivants :

1. Chemin explicite.
1. Le dossier qui contient Aspose.Cells.dll.
1. Le dossier qui contient l'assembly appelé Aspose.Cells.dll.
1. Le dossier qui contient l'assembly d'entrée (votre .exe).
1. Une ressource intégrée dans l'assembly qui a appelé Aspose.Cells.dll.

Le moyen le plus simple de définir une licence consiste à placer le fichier de licence dans le même dossier que le fichier Aspose.Cells.dll et à spécifier le nom du fichier, sans chemin, comme indiqué dans l'exemple ci-dessous.
### **Chargement d'une licence à partir d'un fichier**
Le moyen le plus simple d'appliquer une licence consiste à placer le fichier de licence dans le même dossier que le fichier Aspose.Cells.dll et à spécifier uniquement le nom du fichier sans chemin.

{{% alert color="primary" %}} 

Lorsque vous appelez la méthode SetLicense, le nom de licence que vous transmettez doit être celui du fichier de licence. Par exemple, si vous modifiez le nom du fichier de licence en "Aspose.Cells.lic.xml", transmettez ce nom de fichier à la méthode Cells->SetLicense(…).

{{% /alert %}} 

**C++**

{{< highlight "csharp" >}}

 intrusive_ptr<License> license = new License();

license->SetLicense(new String("Aspose.Cells.lic"));

{{< /highlight >}}
### **Chargement d'une licence à partir d'un objet de flux**
L'exemple suivant montre comment charger une licence à partir d'un flux.

**C++**

{{< highlight "csharp" >}}

 intrusive_ptr<License>license = new License();

intrusive_ptr<FileStream> myStream = new FileStream(new String("Aspose.Cells.lic"), FileMode_Open);

license->SetLicense(myStream);

{{< /highlight >}}
