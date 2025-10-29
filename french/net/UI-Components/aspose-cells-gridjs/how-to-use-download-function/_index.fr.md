---
title: Fonction de téléchargement personnalisé pour GridJs  
type: docs
weight: 260
url: /fr/net/aspose-cells-gridjs/how-to-use-download-function/
description: Cet article décrit comment implémenter une fonction de téléchargement personnalisée pour GridJs.
keywords: GridJs, téléchargement, téléchargement de fichiers, téléchargement personnalisé, export, sauvegarde de fichier
aliases:
  - /net/aspose-cells-gridjs/download-function/
  - /net/aspose-cells-gridjs/how-to-add-download-function/
  - /net/aspose-cells-gridjs/custom-download/
---


# Comment implémenter une fonction de téléchargement personnalisée pour GridJs

GridJs offre un mécanisme de téléchargement flexible qui vous permet de personnaliser le comportement de téléchargement de fichiers. Vous pouvez définir une fonction de téléchargement personnalisée pour gérer les téléchargements en fonction de vos besoins.

## Définir une fonction de téléchargement personnalisée

GridJs fournit la méthode `setFileDownloadCallFunction` pour définir une fonction de téléchargement personnalisée. Lorsque les utilisateurs cliquent sur le bouton de téléchargement, cette fonction sera appelée avec des paramètres spécifiques.

### Usage de base

```javascript
// Define your custom download function
function customDownloadHandler(toFileName, outputType, saveMode) {
    console.log('File Name:', toFileName);
    console.log('Output Type:', outputType);
    console.log('Save Mode:', saveMode);

    // Implement your custom download logic here
    // For example: upload to cloud storage, save to custom location, etc.
}

// Set the custom download function
xs.setFileDownloadCallFunction(customDownloadHandler);
```

## Paramètres de la fonction

La fonction de téléchargement personnalisée reçoit trois paramètres :

### 1. toFileName
- **Type**: Chaîne de caractères
- **Description**: Le nom du fichier à télécharger
- **Exemple**: `"monfichier.xlsx"`, `"rapport.pdf"`

### 2. outputType
- **Type**: Chaîne de caractères
- **Description**: Le format de fichier de sortie
- **Valeurs possibles** :
  - `Original` - Conserver le format de fichier original
  - `XLSX` - Exporter au format Excel
  - `PDF` - Exporter au format PDF
  - `HTML` - Exporter au format HTML

### 3. saveMode
- **Type**: Chaîne de caractères
- **Description**: Le mode de destination de l'enregistrement
- **Valeurs possibles** :
  - `Device` - Télécharger sur l'appareil local (par défaut)
  - `GoogleDrive` - Enregistrer sur Google Drive
  - `Dropbox` - Enregistrer sur Dropbox

## Scénarios de téléchargement

GridJs prend en charge plusieurs scénarios de téléchargement en fonction des actions de l'utilisateur :

### 1. Télécharger dans différents formats

```javascript
function customDownloadHandler(toFileName, outputType, saveMode) {
    switch(outputType) {
        case 'Original':
            // Handle original format download
            downloadAsOriginal(toFileName);
            break;
        case 'XLSX':
            // Handle Excel format download
            downloadAsExcel(toFileName);
            break;
        case 'PDF':
            // Handle PDF format download
            downloadAsPDF(toFileName);
            break;
        case 'HTML':
            // Handle HTML format download
            downloadAsHTML(toFileName);
            break;
    }
}

xs.setFileDownloadCallFunction(customDownloadHandler);
```

### 2. Enregistrer dans le stockage cloud

```javascript
function customDownloadHandler(toFileName, outputType, saveMode) {
    if (saveMode === 'GoogleDrive') {
        // Implement Google Drive upload logic
        uploadToGoogleDrive(toFileName, outputType);
    } else if (saveMode === 'Dropbox') {
        // Implement Dropbox upload logic
        uploadToDropbox(toFileName, outputType);
    } else {
        // Default: download to device
        downloadToDevice(toFileName, outputType);
    }
}

xs.setFileDownloadCallFunction(customDownloadHandler);
```

## Notes

1. **Enregistrement de la fonction** : Assurez-vous d'appeler `setFileDownloadCallFunction` avant que les utilisateurs n'interagissent avec la fonctionnalité de téléchargement.

2. **Gestion des erreurs** : Implémentez toujours une gestion appropriée des erreurs dans votre fonction de téléchargement personnalisée pour fournir un retour aux utilisateurs.

3. **Opérations asynchrones** : Si votre logique de téléchargement implique des opérations asynchrones (comme des appels API), assurez-vous de gérer correctement les promesses.

4. **Extension du nom de fichier** : Lorsque le type de sortie n'est pas "Original", l'extension du fichier sera automatiquement ajustée pour correspondre au type de sortie (par exemple, `.xlsx`, `.pdf`, `.html`).

5. **Comportement par défaut** : Si vous ne définissez pas de fonction de téléchargement personnalisée, GridJs utilisera son comportement de téléchargement par défaut.

## Voir aussi

- [Commencer avec GridJs](/net/aspose-cells-gridjs/getting-started/)
- [Comment construire un éditeur Excel en ligne](/net/aspose-cells-gridjs/how-to-build-online-excel-editor/)
- [Configuration côté serveur](/net/aspose-cells-gridjs/server-side-configuration/)
