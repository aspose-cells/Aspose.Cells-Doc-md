---
title: دليل تكوين متعدد اللغات GridJs
type: docs
weight: 250
url: /ar/java/aspose-cells-gridjs/how-to-configuration-multi-language/
description: سيساعدك هذا الدليل على تكوين دعم متعدد اللغات
keywords: GridJs، متعدد اللغات، التعريب، الدولية، الثقافة، CultureInfo
aliases:
- /java/aspose-cells-gridjs/multi-language/
- /java/aspose-cells-gridjs/multi-language-guide/
- /java/aspose-cells-gridjs/localization-setup/
- /java/aspose-cells-gridjs/multi-language-configuration/
- /java/aspose-cells-gridjs/internationalization-guide/
- /java/aspose-cells-gridjs/culture-configuration/
---

# دليل تكوين متعدد اللغات لـ Aspose.Cells GridJs

## نظرة عامة

سيساعدك هذا الدليل على تكوين دعم متعدد اللغات في مشروع Aspose.Cells GridJs الخاص بك. يغطي التكوينات الأمامية والخلفية على حد سواء.

الدليل مبني على [مشروع العرض التوضيحي](https://github.com/aspose-cells/Aspose.Cells/Grid-for-Java/tree/main/Examples.GridJs)، يرجى التعديل وفقًا للوضع الفعلي

## التكوين الأمامي

في صفحات الواجهة الخاصة بك، قم بتعيين لغة الواجهة باستخدام خيار [local](https://docs.aspose.com/cells/net/aspose-cells-gridjs/how-to-use-gridjs-client-api/).

في مشروع العرض التوضيحي، تحتاج إلى تعديل ملف [uidload.html](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/main/Examples.GridJs/src/main/resources/templates/index.html)

إليك مثال:

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

## التكوين الخلفي

في كود الخلفية، تحتاج إلى ضبط CultureInfo المناسب قبل معالجة بيانات Excel.

في مشروع العرض التوضيحي، تحتاج إلى تعديل ملف [التطبيق](https://github.com/aspose-cells/Aspose.Cells.Grid-for-Java/blob/main/Examples.GridJs/src/main/java/com/aspose/gridjs/demo/GridjsdemoApplication.java)

### تعيين إعدادات اللغة في دالة الرئيسية

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

## ملاحظات مهمة

1. يجب أن تكون إعدادات لغة الواجهة الأمامية والخلفية متطابقة.
2. يجب تعيين CultureInfo قبل معالجة بيانات Excel.
3. اللغات المدعومة: en(الإنجليزية)، zh(الصينية)، es(الإسبانية)، pt(البرتغالية)، de(الألمانية)، ru(الروسية)، nl(الهولندية)، pl(البولندية).
4. يستخدم المثال اللغة البولندية (pl-PL)، ولكن يمكنك تغييرها إلى أي لائحة أخرى مدعومة.
