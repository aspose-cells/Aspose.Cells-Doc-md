---
title: كيفية استخدام Aspose.Cells لـ Python via Java في بيئة Gunicorn+Flask
type: docs
weight: 40
url: /ar/python-java/aspose-cells-python-java-in-gunicorn-flask/
description: via Java يقارن هذا القسم بين Aspose.Cells لـ Python المكونات وبعض مكتبات عمليات Excel الأخرى.
keywords: via Java Excel Python, Excel Python, Excel Python, Excel Python via Java, لماذا Aspose.Cells لـ Python via Java، لماذا لا تستخدم xlrd xlwt xlutils xlwings openpyxl xlswriter win32com DataNitro pandas.
---

{{% alert color="primary" %}}

يُوضح موضوع المبتدئين هذا كيف يمكن للمطورين إنشاء تطبيق بسيط (مرحبًا بالعالم) باستخدام Aspose.Cells لـ Python via Java. ينشئ التطبيق ملف إكسل من مايكروسوفت مكتوب فيه 'مرحبًا بالعالم' في خلية محددة من ورقة عمل.

{{% /alert %}}



## **إعداد البيئة الكاملة**

بيئة تشغيل المثال في هذا الدليل هي Ubuntu: 20.04، يمكنك تعديلها حسب وضعك الفعلي. لضمان عمل الأمثلة بشكل صحيح، نحتاج إلى تثبيت بعض الأدوات الضرورية في البيئة. إليك دليل خطوة بخطوة لمساعدتك على إكمال العملية. يرجى ملاحظة أن هذا مجرد دليل تقريبي، وقد تختلف التفاصيل حسب نظامك واحتياجاتك.

### بايثون

إذا لم يتم تثبيته، قم بتثبيته على النحو التالي:
```
sudo apt install python3 python3-pip # Ubuntu/Debian
#sudo yum install python3 python3-pip # CentOS/RHEL
```
تحقق من الإصدار
```
python3 --version
pip3 --version
```

### Java
إذا لم يتم تثبيته، قم بتثبيته على النحو التالي:
```
sudo apt install openjdk-11-jdk # Ubuntu/Debian
#sudo yum install java-17-openjdk # CentOS/RHEL
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH
```
تحقق من الإصدار
```
java -version
```

### بيئة افتراضية virtualenv
تم تثبيت البيئة الافتراضية بناءً على احتياجاتك الفعلية، يُنصَح باستخدام بيئات افتراضية لإدارة تبعيات المشروع في بيئات التطوير والإنتاج.
يرجى اتباع الأمر التالي للتثبيت:
```
sudo apt install python3-venv # Ubuntu/Debian
#sudo yum install python3-venv # CentOS/RHEL
```
إنشاء بيئة افتراضية
```
python3 -m venv myenv # Create a virtual environment named myenv in the current directory
```
بدء البيئة الافتراضية
```
source myenv/bin/activate
```

***ملاحظة: إذا تم استخدام بيئة افتراضية، يتطلب العمليات التالية تفعيل البيئة الافتراضية المقابلة أولاً***

### فلاسک
إذا لم يتم التثبيت، يرجى اتباع الأمر التالي للتثبيت:
```
pip install Flask
```

### Gunicorn
إذا لم يتم التثبيت، يرجى اتباع الأمر التالي للتثبيت:
```
pip install gunicorn
```

### Jpype
إذا لم يتم التثبيت، يرجى اتباع الأمر التالي للتثبيت:
```
pip install jpype1
```

### aspose-cells
إذا لم يتم التثبيت، يرجى اتباع الأمر التالي للتثبيت:
```
pip install aspose-cells
```

## **إنشاء تطبيق مرحبًا بالعالم**

لإنشاء تطبيق مرحبًا بالعالم باستخدام واجهة برمجة التطبيقات الخاصة بـ Aspose.Cells:

1. أنشئ نسخة من فئة [**Workbook**](https://reference.aspose.com/cells/python-java/asposecells.api/Workbook).
1. طبق الترخيص:
   1. إذا قمت بشراء ترخيص ، فاستخدم الترخيص في تطبيقك للحصول على وصول إلى وظائف Aspose.Cells الكاملة
   1. إذا كنت تستخدم الإصدار التجريبي من المكون (إذا كنت تستخدم Aspose.Cells بدون ترخيص) ، فتخطى هذه الخطوة.
1. إنشاء ملف Microsoft Excel جديد ، أو فتح ملف موجود ترغب في إضافة / تحديث بعض النص فيه.
1. الوصول إلى أي خلية في ورقة العمل في ملف Microsoft Excel.
1. إدراج كلمات **Hello World!** في الخلية التي تم الوصول إليها.
1. إنشاء ملف Microsoft Excel المعدل.

الأمثلة أدناه تظهر الخطوات أعلاه.

### **إنشاء دفتر العمل**

المثال التالي ينشئ دفتر عمل جديد من البداية ، يكتب كلمة "Hello World!" في الخلية A1 في ورق العمل الأول ، ثم يحفظ الملف.

افترض أن لدينا مسار اختبار "/app". سنقوم بالعمل التالي تحت هذا المسار التجريبي.

#### ملفات تطبيق Flask: hello.py

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CreatingHelloWorldFileInFlask1.py" >}}


#### ملف فئة البدء المخصصة ل Gunicorn: custom_gunicorn.py

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CreatingHelloWorldFileInFlask2.py" >}}

#### بدء الخدمة

تحقق من تثبيت جميع الحزم الضرورية للخدمة، ثم ابدأ الخدمة.

إذا كنت تستخدم البيئة الافتراضية python3-venv، فقم بإنشاء بيئة افتراضية في مسار الاختبار، شغّلها، ثم قم بتثبيت جميع حزم الأدوات المطلوبة.

``` 
python custom_gunicorn.py Or python3 custom_gunicorn.py
``` 

#### نتائج الفحص

1. افتح المتصفح وقم بزيارة http://127.0.0.1:5000/.

2. أدخل اسم الملف الذي تريد حفظه في مربّع الإدخال.

3. اضغط على زر 'توليد' لحفظ الملف.

بعد القيام بذلك، ستحصل على ملف إكسل باسم المحتوى الذي أدخلته في مسار الاختبار الحالي. المعاينة كالتالي:

![todo:image_alt_text](HelloWorldFileInFlask.png)


## استخدام Docker

أو يمكنك وضع العمليات أعلاه في حاوية Docker. من السهل جدًا استخدام Docker لبناء البيئة المستخدمة بواسطة المثال. فقط ضع العمليات أعلاه في ملف Dockerfile.

إليك مثال لملف Dockerfile للمرجعة. يعرض بعض أدوات البرمجة الضرورية لبناء البيئة.

### Dockerfile

``` 
FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    python3-venv \
    build-essential \
    libssl-dev \
    libffi-dev \
    libpq-dev \
    openjdk-11-jdk \
    wget \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python3", "custom_gunicorn.py"]
```

### requirements.txt

يستخدم هذا الملف بشكل رئيسي لتوفير بيئة اعتماد لمشاريع بايثون. يمكنك تعديل الإصدار في هذا الملف ليناسب احتياجاتك.

```
aspose-cells==24.11.0
jpype1==1.5.1
Flask==3.0.3
gunicorn==23.0.0
```
### الملفات الرئيسية

هيكل الملفات الرئيسي كالتالي:
```
app/
|-requirements.txt
|-hello.py
|-custom_gunicorn.py
```

### بدء الحاوية

يمكنك بدء الحاوية باستخدام الأمر التالي
```
docker run --rm -p 127.0.0.1:5000:5000 gunicorn_flask:v1.0 # gunicorn_flask:v1.0 - Image built by Dockerfile
```
