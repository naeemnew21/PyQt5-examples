# interface arabic or english
from PyQt5.QtCore import Qt

english_status = [
    'changed' , 'failed' , 'this info written in data' , 'failed' , 'fail-over order' , 'fail-over son',
    'ok but repeated' , 'added' , 'failed' , 'not exist' , 'failed' , 'deleted' , 'failed' , 'saved' ,
    'failed' , 'error' , 'ok' , 'failed' , 'male' , 'female' , 'family name'
    ]
arabic_status = [
    'تغير' , 'فشل التغيير'  , 'ابناء النساء تكتب فى خانة البيانات' , 'فشل الاضافة' , 'فشل السلسلة' , 'فشل لزيادة العدد' ,
    'تم لكنه مكرر' , 'تمت الاضافة' , 'فشل الاضافة' , 'غير موجود' , 'فشل الحذف' , 'تم الحذف' , 'فشل الحذف' , 'تم الحفظ' ,
    'فشل الحفظ' , 'خطأ' , 'تم' , 'فشل' , 'مذكر' , 'مؤنث' , 'اسم العائلة'
    ]

def english_interface(form):
    form.info_box.setTitle('info')
    form.profile_box.setTitle('profile')
    form.search_box.setTitle('search')
    form.setting_box.setTitle('setting')
    form.fam_frame.setTitle('Family Tree')

    form.info_name.setText('name :')
    form.info_son.setText('children :')
    form.info_gender.setText('gender :')
    form.info_data.setText('data :')
    form.info_status.setText('status :')
    form.pro_name.setText('name :')
    form.pro_gender.setText('gender :')
    form.pro_count.setText('family count :')
    form.search_name_label.setText('name :')
    form.search_count_label.setText('count :')

    form.edit_btn.setText('change')
    form.del_btn.setText('Del')
    form.add_btn.setText('add')
    form.save_btn.setText('save')
    form.search_btn.setText('search')
    form.export_btn.setText('save as img')
    form.lang_btn.setText('عربى')

    form.gender_cb.setItemText(0 , 'male')
    form.gender_cb.setItemText(1 , 'female')
    

    
def arabic_interface(form):
    form.info_box.setTitle('معلومات ')
    form.profile_box.setTitle('البروفايل ')
    form.search_box.setTitle('البحث ')
    form.setting_box.setTitle('الضبط ')
    form.fam_frame.setTitle('شجرة العائلة ')

    form.info_name.setText('الاسم :')
    form.info_son.setText('الاولاد :')
    form.info_gender.setText('النوع :')
    form.info_data.setText('البيانات :')
    form.info_status.setText('الحالة :')
    form.pro_name.setText('الاسم :')
    form.pro_gender.setText('النوع :')
    form.pro_count.setText('عدد النسل :')
    form.search_name_label.setText('الاسم :')
    form.search_count_label.setText('العدد :')

    form.edit_btn.setText('تغيير')
    form.del_btn.setText('حذف')
    form.add_btn.setText('اضافة')
    form.save_btn.setText('حفظ')
    form.search_btn.setText('بحث')
    form.export_btn.setText('حفظ كصورة')
    form.lang_btn.setText('English')

    form.gender_cb.setItemText(0 , 'مذكر')
    form.gender_cb.setItemText(1 , 'مؤنث')


def reverse_layout(form , n) :
    form.setting_box.setLayoutDirection(n)
    form.search_box.setLayoutDirection(n)
    form.profile_box.setLayoutDirection(n)
    form.info_box.setLayoutDirection(n)
    form.fam_frame.setLayoutDirection(n)
    if n== 0:
        form.profile_count.setAlignment(Qt.AlignLeft )
    else :
        form.profile_count.setAlignment(Qt.AlignRight)
               
