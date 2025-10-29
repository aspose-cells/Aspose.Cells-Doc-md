---
title: Guide de configuration multilingue de GridJs
type: docs
weight: 250
url: /fr/java/aspose-cells-gridjs/how-to-configuration-multi-language/
description: Ce tutoriel vous guidera dans la configuration du support multilingue
keywords: GridJs, multilingue, localisation, internationalisation, culture, CultureInfo
aliases:
- /java/aspose-cells-gridjs/multi-language/
- /java/aspose-cells-gridjs/multi-language-guide/
- /java/aspose-cells-gridjs/localization-setup/
- /java/aspose-cells-gridjs/multi-language-configuration/
- /java/aspose-cells-gridjs/internationalization-guide/
- /java/aspose-cells-gridjs/culture-configuration/
---

# Guide de configuration multilingue Aspose.Cells GridJs

## Aperçu

Ce tutoriel vous guidera dans la configuration du support multilingue dans votre projet Aspose.Cells GridJs. Il couvre les configurations côté frontend et backend.

Le tutoriel est basé sur le [projet de démonstration](https://github.com/aspose-cells/Aspose.Cells/Grid-for-Java/tree/main/Examples.GridJs), veuillez l'ajuster en fonction de la situation réelle

## Configuration frontend

Dans vos pages frontend, définissez la langue de l'interface avec l'option `local` [option](https://docs.aspose.com/cells/net/aspose-cells-gridjs/how-to-use-gridjs-client-api/).

Dans le projet de démonstration, vous devez modifier le fichier [uidload.html](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/main/Examples.GridJs/src/main/resources/templates/index.html)

Voici un exemple :

```javascript
const loadNormalContext = (sheet) => {
    const option = {
        updateMode: 'server',
        updateUrl: '/GridJs2/UpdateCell',
        showToolbar: true,
        mode: 'edit',
        // Supported languages: en/zh/es/pt/de/ru/nl/pl
        local: 'pl', // Set to Polish in this example
    };
    loadWithOption(jsondata, option);
};
```

## Configuration backend

Dans le code backend, vous devez définir le CultureInfo approprié avant de traiter les données Excel.

Dans le projet de démonstration, vous devez modifier le fichier [Application](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/main/Examples.GridJs/src/main/java/com/aspose/gridjs/demo/GridjsdemoApplication.java)

### définir les paramètres régionaux dans la méthode principale

```java

public static void main(String[] args) {

	// Set Polish locale for current thread
        Locale polishLocale = new Locale("pl", "PL");
        Locale.setDefault(polishLocale);

        // Demonstration of locale settings
        System.out.println("Current Locale: " + Locale.getDefault());

		 ApplicationContext context  = 	SpringApplication.run(GridjsdemoApplication.class, args);

		 MyConfig myConfig = context.getBean(MyConfig.class);

		 //set license for Aspose.Cells
		 com.aspose.cells.License  lic=new com.aspose.cells.License();
			if ((new File(myConfig.asposeLicensePath)).exists()) {
				lic.setLicense(myConfig.asposeLicensePath);
			}


	}

```

## Notes importantes

1. Les paramètres de langue du frontend et du backend doivent être cohérents.
2. Le CultureInfo doit être défini avant le traitement des données Excel.
3. Langues prises en charge : en (Anglais), zh (Chinois), es (Espagnol), pt (Portuguais), de (Allemand), ru (Russe), nl (Néerlandais), pl (Polonais).
4. L'exemple utilise le polonais (pl-PL), mais vous pouvez le changer pour toute autre locale supportée.
