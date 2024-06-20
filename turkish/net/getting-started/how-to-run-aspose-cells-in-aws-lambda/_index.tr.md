---
title: AWS Lambda da Aspose.Cells Nasıl Çalıştırılır
type: docs
description: Aspose.Cells işlevselliğini uygulamanıza, geliştirme yığınızda hangi teknolojiyi kullanmış olursanız olun Docker kullanarak entegre edin. Bir Docker konteynerinde Aspose.Cells i nasıl kullanacağınızı öğrenin.
weight: 141
url: /tr/net/how-to-run-aspose-cells-in-aws-lambda/
---

## AWS Ortamını Hazırlama

1. Bir AWS hesabı kaydedin: 
[AWS hesabı kaydı](https://aws.amazon.com/)
1. AWS hesabınıza giriş yapın, hesabınız altına bir IAM kullanıcısı ekleyin. AWS resmi belgelerine başvurabilirsiniz:
[IAM kullanıcısı eklemek](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html)
1. “AmazonS3FullAccess” iznini ekleyin, her biri için aynı şekilde, EC2 ve Elastic Beanstalk için tam erişim ekleyin.
1. Son adımda, IAM kullanıcı adınızı, Anahtarı, Anahtar Kimliğini ve “credentials.csv” dosyasını aldığınızdan emin olun, onları iyi saklamanız gerekmektedir.
   Şimdi IAM kullanıcınızda S3, EC2, Elastic Beanstalk, tam erişime sahip olduğundan emin olun. bkz:

**![AWS Erişimi](AwsErisim.png)**

## Visual Studio için AWS Toolkit'i Yükle

1. Visual Studio 2019 veya üstü sürümünü yükleyin.
1. Visual Studio için AWS Toolkit'i indirin ve yükleyin: 
[AWS Toolkit](https://aws.amazon.com/visualstudio/)

## AWS Lambda'da Çalışan Bir Proje Oluşturun

1. Visual Studio'da bir ASP.NET Core Web Uygulaması oluşturun, test kodu yazın, nuget'ten Aspose.Cells'i alın.

1. Test projesinin yerel makinenizde iyi çalıştığından emin olun, ardından AWS Elastic Beanstalk'e dağıtın:
   Projeyi sağ tıklayıp "AWS Elastic Beanstalk'e Yayımla" seçeneğini seçin. (Bu seçenek yalnızca AWS Toolkit'in Visual Studio'ya kurulmasından sonra mevcut olacaktır). 
1. AWS hesabınız ve IAM kullanıcısıyla yeni bir kullanıcı eklemeniz gerekecektir, önceki adımda elde ettiğiniz "credentials.csv" dosyasını içe aktarabilirsiniz. 
1. Yayımlama başarılı ise, `http://testprojectaspose-test.us-west-2.elasticbeanstalk.com/` gibi bir bağlantı adresi alacaksınız.
   Bağlantının geçerli olması için 10 dakika bekleyin, ardından ziyaret edebilirsiniz!
