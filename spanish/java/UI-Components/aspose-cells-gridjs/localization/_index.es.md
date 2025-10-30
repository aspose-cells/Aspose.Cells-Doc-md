---
title: Guía de configuración multilingüe de GridJs
type: docs
weight: 250
url: /es/java/aspose-cells-gridjs/how-to-configuration-multi-language/
description: Esta tutorial te guiará en la configuración del soporte multilenguaje
keywords: GridJs, multilenguaje, localización, internacionalización, cultura, CultureInfo
aliases:
- /java/aspose-cells-gridjs/multi-language/
- /java/aspose-cells-gridjs/multi-language-guide/
- /java/aspose-cells-gridjs/localization-setup/
- /java/aspose-cells-gridjs/multi-language-configuration/
- /java/aspose-cells-gridjs/internationalization-guide/
- /java/aspose-cells-gridjs/culture-configuration/
---

# Guía de configuración multilingual de Aspose.Cells GridJs

## Resumen

Este tutorial te guiará en la configuración del soporte multilenguaje en tu proyecto Aspose.Cells GridJs. Cubre configuraciones tanto del frontend como del backend.

La guía está basada en el [proyecto de demo](https://github.com/aspose-cells/Aspose.Cells/Grid-for-Java/tree/main/Examples.GridJs), por favor ajústela según la situación actual

## Configuración del frontend

En sus páginas frontend, configure el idioma de la interfaz usando la opción [local](https://docs.aspose.com/cells/net/aspose-cells-gridjs/how-to-use-gridjs-client-api/)

En el proyecto de demo, necesita modificar el archivo [uidload.html](https://github.com/aspose-cells/Aspose.Cells/Grid-for-Java/blob/main/Examples.GridJs/src/main/resources/templates/index.html)

Aquí tienes un ejemplo:

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

## Configuración del backend

En el código backend, necesitas establecer la CultureInfo apropiada antes de procesar datos de Excel.

En el proyecto de demostración, necesitas modificar el archivo [Application](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/main/Examples.GridJs/src/main/java/com/aspose/gridjs/demo/GridjsdemoApplication.java)

### configurar ajustes regionales en el método principal

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

## Notas importantes

1. Las configuraciones de idioma en frontend y backend deben ser coherentes.
2. La cultura (CultureInfo) debe establecerse antes de procesar datos de Excel.
3. Idiomas soportados: en (Inglés), zh (Chino), es (Español), pt (Portugués), de (Alemán), ru (Ruso), nl (Holandés), pl (Polaco).
4. El ejemplo usa polaco (pl-PL), pero puedes cambiarlo por cualquier otra localidad compatible.
