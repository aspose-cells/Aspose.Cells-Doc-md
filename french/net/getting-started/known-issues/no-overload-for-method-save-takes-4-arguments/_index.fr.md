---
title: Aucune surcharge de la méthode Enregistrer ne prend 4 arguments
type: docs
weight: 70
url: /fr/net/no-overload-for-method-save-takes-4-arguments/
---

## **Symptôme**

"En utilisant la version Aspose.Cells, j'obtiens cette erreur lorsque j'utilise la méthode Enregistrer pour tenter d'enregistrer le classeur dans l'objet Réponse. J'ai trouvé ce fragment de code documenté dans la documentation en ligne."

### **Capture d'écran de l'erreur**

![todo:image_alt_text](no-overload-for-method-save-takes-4-arguments_1.png)

### **Solution**

Please use **.NET 2.0** compiled version of the product as it works fine on VS.NET 2008/2010. Actually we provide separate dll's for different environments, project types and systems etc. For reference, please check:<https://docs.aspose.com/cells/net/using-aspose-cells-on-32-bit-and-64-bit-platforms/>

Aspose.Cells for .NET est compatible et fonctionne bien avec toutes les versions du framework .NET, c'est-à-dire 2.x, 3.x, 4.x, etc. pour tout type de projet, par exemple Asp.NET/Winforms, projet Web, application console ou autres projets, etc. Nous fournissons différents fichiers DLL pour différentes versions du framework .NET. Pour plus d'informations, veuillez lire le fichier **readme.txt** dans le dossier "\Bin" à votre répertoire d'installation. Cependant, ce fichier **readme.txt** est présent.

Lorsque vous utilisez notre produit dans une application Web, veuillez utiliser Aspose.Cells.dll du dossier **NET 2.0** dans le répertoire "/bin". Pour votre information, le fichier dll dans le répertoire **.NET 3.5 Client Profile** est utilisé uniquement pour l'application console avec le profil client du framework .NET comme framework cible de VS.NET. Veuillez vérifier votre projet, il est possible que votre projet fasse référence à ce fichier dll.

### **Références**

<https://forum.aspose.com/t/overload-for-method-save-of-workbook-takes-4-arguments-involving-response-object/121465/1>
