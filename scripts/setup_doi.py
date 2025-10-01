#!/usr/bin/env python3
"""
АВТОМАТИЧЕСКАЯ НАСТРОЙКА DOI
============================

Создает все необходимые файлы для получения DOI через Zenodo/Figshare

Автор: Optical Connectome Research Team
"""

import os
import shutil
import subprocess
import yaml
from datetime import datetime

def create_data_archive():
    """Создать архив данных для загрузки"""
    print("📦 СОЗДАНИЕ АРХИВА ДАННЫХ...")
    
    # Создаем папку для архива
    archive_dir = "optical_connectome_data"
    if os.path.exists(archive_dir):
        shutil.rmtree(archive_dir)
    os.makedirs(archive_dir)
    
    # Файлы для включения
    files_to_copy = [
        "ds006181_fixed_metrics.csv",
        "multi_dataset_optical_metrics.csv", 
        "optical_connectome_pipeline.py",
        "create_publication_figures.py",
        "enhanced_statistics.py",
        "fix_constant_metrics.py",
        "arxiv_preprint_final.md",
        "Statistical_Report.md",
        "Figure1_Distributions.png",
        "Figure2_Correlations.png", 
        "Figure3_3D_Tracts.png",
        "Figure4_Network.png",
        "Figure5_Dataset_Comparison.png",
        "ROC_Analysis.png"
    ]
    
    # Копируем файлы
    copied_files = []
    for file in files_to_copy:
        if os.path.exists(file):
            shutil.copy2(file, archive_dir)
            copied_files.append(file)
            print(f"  ✅ {file}")
        else:
            print(f"  ⚠️  {file} не найден")
    
    # Создаем README для архива
    readme_content = f"""# Optical Connectome Analysis Dataset

## Описание
Полный набор данных для анализа оптического коннектома мозга человека.

## Содержимое
- ds006181_fixed_metrics.csv - основные метрики (1,200 трактов)
- multi_dataset_optical_metrics.csv - мультидатасетный анализ
- *.py - код анализа
- *.md - документация
- *.png - графики

## Использование
См. optical_connectome_pipeline.py для полного анализа.

## Лицензия
CC BY 4.0

## Дата создания
{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Авторы
Optical Connectome Research Team

## Связанные публикации
[To be added upon publication]
"""
    
    with open(f"{archive_dir}/README.md", "w") as f:
        f.write(readme_content)
    
    print(f"✅ README создан")
    
    # Создаем архив
    archive_name = "optical_connectome_data.tar.gz"
    if os.path.exists(archive_name):
        os.remove(archive_name)
    
    subprocess.run(["tar", "-czf", archive_name, archive_dir])
    print(f"✅ Архив создан: {archive_name}")
    
    return archive_name, copied_files

def create_citation_file():
    """Создать CITATION.cff файл"""
    print("📝 СОЗДАНИЕ CITATION.CFF...")
    
    citation_data = {
        "cff-version": "1.2.0",
        "message": "If you use this software, please cite it as below.",
        "authors": [
            {
                "given-names": "Optical",
                "family-names": "Connectome Research Team",
                "orcid": "https://orcid.org/0000-0000-0000-0000"
            }
        ],
        "title": "Optical Connectome Analysis of Human Brain",
        "version": "1.0.0",
        "date-released": "2024-12-01",
        "url": "https://github.com/optical-connectome/optical-connectome-analysis",
        "license": "MIT",
        "keywords": [
            "optical connectome",
            "bio-photonic", 
            "brain",
            "MRI",
            "neuroscience"
        ]
    }
    
    with open("CITATION.cff", "w") as f:
        yaml.dump(citation_data, f, default_flow_style=False)
    
    print("✅ CITATION.cff создан")

def create_github_files():
    """Создать файлы для GitHub"""
    print("🐙 СОЗДАНИЕ GITHUB ФАЙЛОВ...")
    
    # .gitignore
    gitignore_content = """*.pyc
__pycache__/
*.log
.DS_Store
venv/
*.egg-info/
*.tar.gz
optical_connectome_data/
"""
    
    with open(".gitignore", "w") as f:
        f.write(gitignore_content)
    
    # README.md для GitHub
    github_readme = """# Optical Connectome Analysis

## Описание
Анализ оптического коннектома мозга человека с использованием диффузионной МРТ и оптической модели волноводов.

## Установка
```bash
pip install -r requirements.txt
```

## Использование
```bash
python optical_connectome_pipeline.py
```

## Результаты
- 1,200 трактов проанализировано
- Новые метрики сложности (DEA, KACI)
- Полная статистика и визуализация

## Лицензия
MIT

## Цитирование
См. CITATION.cff
"""
    
    with open("README.md", "w") as f:
        f.write(github_readme)
    
    # requirements.txt
    requirements = """numpy>=1.21.0
pandas>=1.3.0
matplotlib>=3.4.0
seaborn>=0.11.0
scipy>=1.7.0
scikit-learn>=1.0.0
networkx>=2.6.0
nibabel>=3.2.0
dipy>=1.4.0
"""
    
    with open("requirements.txt", "w") as f:
        f.write(requirements)
    
    print("✅ GitHub файлы созданы")

def create_zenodo_metadata():
    """Создать метаданные для Zenodo"""
    print("📋 СОЗДАНИЕ МЕТАДАННЫХ ZENODO...")
    
    metadata = {
        "title": "Optical Connectome Analysis Dataset",
        "description": "Complete dataset for optical connectome analysis of human brain using diffusion MRI and optical waveguide modeling",
        "creators": [
            {
                "name": "Optical Connectome Research Team",
                "affiliation": "Research Institution"
            }
        ],
        "keywords": [
            "optical connectome",
            "bio-photonic communication", 
            "brain connectivity",
            "diffusion MRI",
            "waveguide modeling",
            "neuroscience"
        ],
        "license": "CC-BY-4.0",
        "upload_type": "dataset",
        "publication_date": "2024-12-01",
        "access_right": "open"
    }
    
    with open("zenodo_metadata.json", "w") as f:
        import json
        json.dump(metadata, f, indent=2)
    
    print("✅ Метаданные Zenodo созданы")

def create_upload_instructions():
    """Создать инструкции по загрузке"""
    print("📖 СОЗДАНИЕ ИНСТРУКЦИЙ...")
    
    instructions = """# ИНСТРУКЦИИ ПО ЗАГРУЗКЕ НА ZENODO

## 1. Подготовка завершена ✅
- Архив создан: optical_connectome_data.tar.gz
- Метаданные готовы: zenodo_metadata.json
- GitHub файлы созданы

## 2. Загрузка на Zenodo
1. Перейти на https://zenodo.org
2. Войти в аккаунт
3. Нажать "Upload"
4. Загрузить файл: optical_connectome_data.tar.gz
5. Заполнить метаданные (использовать zenodo_metadata.json)
6. Опубликовать
7. Скопировать DOI

## 3. Обновление рукописи
Заменить в arxiv_preprint_final.md:
```markdown
**DOI**: [ЗАМЕНИТЬ НА РЕАЛЬНЫЙ DOI]
```

## 4. Создание GitHub репозитория
1. Создать репозиторий на GitHub
2. Загрузить все файлы
3. Обновить URL в рукописи

## 5. Финальная проверка
- [ ] DOI получен
- [ ] GitHub создан
- [ ] Рукопись обновлена
- [ ] Все файлы проверены

## Готово! 🎉
"""
    
    with open("UPLOAD_INSTRUCTIONS.md", "w") as f:
        f.write(instructions)
    
    print("✅ Инструкции созданы")

def main():
    """Основная функция"""
    print("🚀 АВТОМАТИЧЕСКАЯ НАСТРОЙКА DOI")
    print("=" * 50)
    
    try:
        # 1. Создаем архив данных
        archive_name, copied_files = create_data_archive()
        
        # 2. Создаем CITATION.cff
        create_citation_file()
        
        # 3. Создаем GitHub файлы
        create_github_files()
        
        # 4. Создаем метаданные Zenodo
        create_zenodo_metadata()
        
        # 5. Создаем инструкции
        create_upload_instructions()
        
        print("\n🎉 ВСЕ ГОТОВО!")
        print("=" * 30)
        print("📁 Созданные файлы:")
        print(f"   - {archive_name} (архив для загрузки)")
        print("   - CITATION.cff (цитирование)")
        print("   - .gitignore (GitHub)")
        print("   - README.md (GitHub)")
        print("   - requirements.txt (зависимости)")
        print("   - zenodo_metadata.json (метаданные)")
        print("   - UPLOAD_INSTRUCTIONS.md (инструкции)")
        print("\n✅ Готово для загрузки на Zenodo!")
        print("📖 Следуйте инструкциям в UPLOAD_INSTRUCTIONS.md")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
