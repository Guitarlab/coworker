from django.test import TestCase
from models import Profile, Skill, Project


# Create your tests here.

class SkillTest(TestCase):
    
    def setUp(self):
        self.profile = Profile.objects.create(github_account_id='test_profile_id')

    def create_skill(self, skill_description='Python', level=80):
    	return Skill.objects.create(
            skill_description=skill_description,
            owner=self.profile,
            level=level)

    def test_skill_creation(self):
    	skill = self.create_skill()
    	self.assertTrue(isinstance(skill, Skill))
        self.assertTrue(skill.skill_description, 'Python')
        self.assertTrue(skill.level, 80)


class ProjectTest(TestCase):

	def setUp(self):
		self.profile = Profile.objects.create(github_account_id='test_profile_id')
        self.skill = Skill.objects.create(skill_description='Python', level=80)


	def create_project(self, project_status="Gods' creation"):
		return Project.objects.create(
			project_status=project_status,
			skill=self.skill,
			project_owner=self.profile,
			project_helper=self.profile)

	def test_project_creation(self):
		project = self.create_project()
		self.assertTrue(isinstance(project, Project))
		self.assertTrue(project.project_status, "Gods' creation")
		self.assertTrue(project.project_owner, 'test_profile_id')
		self.assertTrue(project.project_helper, 'test_profile_id')



