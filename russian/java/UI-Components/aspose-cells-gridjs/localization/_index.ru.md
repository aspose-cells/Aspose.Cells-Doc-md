---
title: Руководство по настройке мультиязыковой поддержки GridJs
type: docs
weight: 250
url: /ru/java/aspose-cells-gridjs/how-to-configuration-multi-language/
description: Это руководство проведет вас по настройке поддержки нескольких языков
keywords: GridJs, мультиязычность, локализация, интернационализация, культура, CultureInfo
aliases:
- /java/aspose-cells-gridjs/multi-language/
- /java/aspose-cells-gridjs/multi-language-guide/
- /java/aspose-cells-gridjs/localization-setup/
- /java/aspose-cells-gridjs/multi-language-configuration/
- /java/aspose-cells-gridjs/internationalization-guide/
- /java/aspose-cells-gridjs/culture-configuration/
---

# Руководство по настройке мультиязыковой поддержки Aspose.Cells GridJs

## Обзор

Это руководство проведет вас по настройке мультиязыковой поддержки в вашем проекте Aspose.Cells GridJs. Оно охватывает как фронтенд, так и бэкенд настройки.

Обучение основано на [демо проекте](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/tree/main/Examples.GridJs), пожалуйста, адаптируйте его в соответствии с фактической ситуацией

## Конфигурация фронтенда

На своих фронтенд-страницах установите язык интерфейса, используя опцию [`local`](https://docs.aspose.com/cells/net/aspose-cells-gridjs/how-to-use-gridjs-client-api/).

В демонстрационном проекте необходимо изменить файл [uidload.html](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/main/Examples.GridJs/src/main/resources/templates/index.html)

Вот пример:

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

## Конфигурация бэкенда

В коде бэкенда необходимо установить соответствующий CultureInfo перед обработкой данных Excel.

В демонстрационном проекте необходимо изменить файл [Application](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/main/Examples.GridJs/src/main/java/com/aspose/gridjs/demo/GridjsdemoApplication.java)

### установка настроек локали в основном методе

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

## Важные заметки

1. Языковые настройки фронтенда и бэкенда должны совпадать.
2. CultureInfo должен быть установлен перед обработкой данных Excel.
3. Поддерживаемые языки: en(английский), zh(китайский), es(испанский), pt(португальский), de(немецкий), ru(русский), nl(голландский), pl(польский).
4. В примере используется польский (pl-PL), но его можно изменить на любой другой поддерживаемый язык.
