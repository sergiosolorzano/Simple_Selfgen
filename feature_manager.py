#!/usr/bin/env python3

#import class
import feature_common as ft_common
#import feature request classes
import ft_requests.feature_request_utest as ft_req_utest
import ft_requests.feature_request_loadcode as ft_req_loadcode
import ft_requests.feature_request_rawcode as ft_req_raw
import ft_requests.feature_request_argparse as ft_req_argparse
import ft_requests.feature_request_excpt_and_log as ft_req_excpt_and_log
import ft_requests.feature_request_runutests as ft_req_run_utests
import ft_requests.feature_request_custom_req as ft_req_custom_req
import ft_requests.feature_request_debuglogs as ft_req_deblogs
import ft_requests.feature_request_docstrings as ft_req_docstrings

#manage feature children classes
class Feature_Manager:

	#init feature children
	def __init__(self):
		#instantiate feature common class
		self.feature_common_instance = ft_common.Feature_Common()
		self.feature_instance = None
		self.ready_to_prepare_request_args = False
		self.back_to_menu = False
		self.request_args = None

		#dict of feature instances, pass shared common instance
		self.feature_instances = {
		'1': ft_req_raw.Feature_Request_Rawcode(self.feature_common_instance),
		'2': ft_req_loadcode.Feature_Request_Loadcode(self.feature_common_instance),
		'3': ft_req_argparse.Feature_Request_Argparse(self.feature_common_instance),
		'4': ft_req_excpt_and_log.Feature_Request_ExceptionHndl_and_Logging(self.feature_common_instance),
		#'5': ft_req_utest.Feature_Request_Utest(self.feature_common_instance), #removed due to underpeformance
		#'6': ft_req_run_utests.Feature_Request_Run_Unit_Test_Cases(self.feature_common_instance), #removed due to underpeformance
		'5': ft_req_custom_req.Feature_Request_CustomRequest(self.feature_common_instance),
		'6': ft_req_deblogs.Feature_Request_DebugLogs(self.feature_common_instance),
		'7': ft_req_docstrings.Feature_Request_Docstrings(self.feature_common_instance)
		}

	def handle_menu_choice(self, choice):
		print("At handle_menu_choice choice", choice)
		#get feature instance according to menu choice
		self.feature_instance = self.feature_instances[choice]

		#meet requirements to request args
		if not self.ready_to_prepare_request_args:
			self.ready_to_prepare_request_args, self.back_to_menu = self.feature_instance.prerequest_args_process()

		#get request args
		if self.ready_to_prepare_request_args and self.request_args is None:
			self.request_args = self.feature_instance.prepare_request_args()
		# do not return back to menu
		return self.feature_instance.request_code(*self.request_args), self.back_to_menu

		#return back to menu
		#return True, self.back_to_menu

	def process_valid_response(self):
		self.reset_vars_end_process()
		return self.feature_instance.process_successful_response()

	def reset_vars_end_process(self):
		print("Resetting vars at manager")
		self.ready_to_prepare_request_args=False
		self.request_args = None
		self.back_to_menu = False
		self.request_args = None


