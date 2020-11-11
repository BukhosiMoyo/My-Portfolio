from django.contrib import admin
from .models import Person, Skill, Experience, Education, Stat, ImagePortfolio, SliderPortfolio, LocalVideoPortfolio, YoutubeVideoPortfolio, Social


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'health', 'phone', 'email', 'skype')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'badge' )


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'start_date', 'end_date')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('name', 'school', 'start_date', 'end_date')


@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ('name', 'years_of_experience', 'projects_completed', 'happy_clients', 'awards_won' )


admin.site.register(ImagePortfolio)

admin.site.register(SliderPortfolio)

admin.site.register(LocalVideoPortfolio)

admin.site.register(YoutubeVideoPortfolio)

@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('name', 'social_link')

