import os
from os import mkdir

from odyssey import Odyssey
from odyssey.utils import config
from odyssey.utils.logger import get_logger
from odyssey.agents.llama import ModelType

import traceback
logger = get_logger('main')
mc_port = config.get('MC_SERVER_PORT')
mc_host = config.get('MC_SERVER_HOST')
node_port = config.get('NODE_SERVER_PORT')
embedding_dir = config.get('SENTENT_EMBEDDING_DIR')
env_wait_ticks = 100

def test_subgoal():
    odyssey_l3_8b = Odyssey(
        mc_port=mc_port,
        mc_host=mc_host,
        env_wait_ticks=env_wait_ticks,
        skill_library_dir="./skill_library",
        reload=True, # set to True if the skill_json updated
        embedding_dir=embedding_dir, # your model path
        environment='subgoal',
        resume=False,
        server_port=node_port,
        critic_agent_model_name = ModelType.LLAMA3_8B_V3,
        comment_agent_model_name = ModelType.LLAMA3_8B_V3,
        planner_agent_qa_model_name = ModelType.LLAMA3_8B_V3,
        planner_agent_model_name = ModelType.LLAMA3_8B_V3,
        action_agent_model_name = ModelType.LLAMA3_8B_V3,
    )
    odyssey_l3_70b = Odyssey(
        mc_port=mc_port,
        mc_host=mc_host,
        env_wait_ticks=env_wait_ticks,
        skill_library_dir="./skill_library",
        reload=True, # set to True if the skill_json updated
        embedding_dir=embedding_dir, # your model path
        environment='subgoal',
        resume=False,
        server_port=node_port,
        critic_agent_model_name = ModelType.LLAMA3_70B_V1,
        comment_agent_model_name = ModelType.LLAMA3_70B_V1,
        planner_agent_qa_model_name = ModelType.LLAMA3_70B_V1,
        planner_agent_model_name = ModelType.LLAMA3_70B_V1,
        action_agent_model_name = ModelType.LLAMA3_70B_V1,
    )
    # 5 classic MC tasks
    test_sub_goals = ["craft crafting table", "craft wooden pickaxe", "craft stone pickaxe", "craft iron pickaxe", "mine diamond"]
    # test_sub_goals = ["mine diamond"]
    while True:
        try:
            odyssey_l3_8b.inference_sub_goal(task="subgoal_llama3_8b_v3", sub_goals=test_sub_goals)
            # odyssey_l3_70b.inference_sub_goal(task="subgoal_llama3_70b_v1", sub_goals=test_sub_goals)
        except Exception as e:
            logger.critical(e)
            traceback.print_exc()

def test_combat():
    odyssey_l3_8b_v3 = Odyssey(
        mc_port=mc_port,
        mc_host=mc_host,
        env_wait_ticks=env_wait_ticks,
        skill_library_dir="./skill_library",
        reload=True, # set to True if the skill_json updated
        embedding_dir=embedding_dir, # your model path
        environment='combat',
        resume=False,
        server_port=node_port,
        critic_agent_model_name = ModelType.LLAMA3_8B_V3,
        comment_agent_model_name = ModelType.LLAMA3_8B_V3,
        planner_agent_qa_model_name = ModelType.LLAMA3_8B_V3,
        planner_agent_model_name = ModelType.LLAMA3_8B_V3,
        action_agent_model_name = ModelType.LLAMA3_8B_V3,
    )
    odyssey_l3_8b = Odyssey(
        mc_port=mc_port,
        mc_host=mc_host,
        env_wait_ticks=env_wait_ticks,
        skill_library_dir="./skill_library",
        reload=True, # set to True if the skill_json updated
        embedding_dir=embedding_dir, # your model path
        environment='combat',
        resume=False,
        server_port=node_port,
        critic_agent_model_name = ModelType.LLAMA3_8B,
        comment_agent_model_name = ModelType.LLAMA3_8B,
        planner_agent_qa_model_name = ModelType.LLAMA3_8B,
        planner_agent_model_name = ModelType.LLAMA3_8B,
        action_agent_model_name = ModelType.LLAMA3_8B,
    )
    odyssey_l3_70b = Odyssey(
        mc_port=mc_port,
        mc_host=mc_host,
        env_wait_ticks=env_wait_ticks,
        skill_library_dir="./skill_library",
        reload=True, # set to True if the skill_json updated
        embedding_dir=embedding_dir, # your model path
        environment='combat',
        resume=False,
        server_port=node_port,
        critic_agent_model_name = ModelType.LLAMA3_70B_V1,
        comment_agent_model_name = ModelType.LLAMA3_70B_V1,
        planner_agent_qa_model_name = ModelType.LLAMA3_70B_V1,
        planner_agent_model_name = ModelType.LLAMA3_70B_V1,
        action_agent_model_name = ModelType.LLAMA3_70B_V1,
    )
    
    multi_rounds_tasks = ["1 zombie", "1 skeleton", "1 spider"]
    l8_v3_combat_benchmark = [
                        # Single-mob tasks
                        "1 skeleton",  "1 spider", "1 zombified_piglin", "1 zombie",
                        # Multi-mob tasks
                        "1 zombie, 1 skeleton", "1 zombie, 1 spider", "1 zombie, 1 skeleton, 1 spider", "3 zombie"
                        ]
    l8_combat_benchmark = [
                        # Single-mob tasks
                         "1 skeleton",  "1 spider", "1 zombified_piglin", "1 zombie",
                        # Multi-mob tasks
                        "1 zombie, 1 skeleton", "1 zombie, 1 spider", "1 zombie, 1 skeleton, 1 spider", "3 zombie"
                        ]
    l70_v1_combat_benchmark = [
                        # Single-mob tasks
                         "1 skeleton",  "1 spider", "1 zombified_piglin", "1 zombie",
                        # Multi-mob tasks
                        "1 zombie, 1 skeleton", "1 zombie, 1 spider", "1 zombie, 1 skeleton, 1 spider", "3 zombie"
                        ]
    MAX_RETRY  = 3
    retry = MAX_RETRY
    while True:
        # for task in combat_benchmark:
        retry = MAX_RETRY
        i = 0
        while i < len(l8_combat_benchmark):
            try:
                odyssey_l3_8b.inference(task=l8_combat_benchmark[i], reset_env=False, feedback_rounds=1)
                i += 1
                retry = MAX_RETRY
            except Exception as e:
                logger.critical(l8_combat_benchmark[i]+' failed. retry...')
                logger.critical(e)
                traceback.print_exc()
                if retry > 0:
                    retry -= 1
                    continue
                i += 1
                retry = MAX_RETRY
        i = 0
        while i < len(multi_rounds_tasks):
            try:
                odyssey_l3_8b.inference(task=multi_rounds_tasks[i], reset_env=False, feedback_rounds=3)
                i += 1
                retry = MAX_RETRY
            except Exception as e:
                logger.critical(multi_rounds_tasks[i]+' failed. retry...')
                logger.critical(e)
                traceback.print_exc()
                if retry > 0:
                    retry -= 1
                    continue
                i += 1
                retry = MAX_RETRY
        # i = 0
        # while i < len(l70_v1_combat_benchmark):
        #     try:
        #         odyssey_l3_70b.inference(task=l70_v1_combat_benchmark[i], reset_env=False, feedback_rounds=1)
        #         i += 1
        #         retry = MAX_RETRY
        #     except Exception as e:
        #         logger.critical(l70_v1_combat_benchmark[i]+' failed. retry...')
        #         logger.critical(e)
        #         traceback.print_exc()
        #         if retry > 0:
        #             retry -= 1
        #             continue
        #         i += 1
        #         retry = MAX_RETRY
        # i = 0
        # while i < len(multi_rounds_tasks):
        #     try:
        #         odyssey_l3_70b.inference(task=multi_rounds_tasks[i], reset_env=False, feedback_rounds=3)
        #         i += 1
        #         retry = MAX_RETRY
        #     except Exception as e:
        #         logger.critical(multi_rounds_tasks[i]+' failed. retry...')
        #         logger.critical(e)
        #         traceback.print_exc()
        #         if retry > 0:
        #             retry -= 1
        #             continue
        #         i += 1
        #         retry = MAX_RETRY
        # i = 0
        # while i < len(l8_v3_combat_benchmark):
        #     try:
        #         odyssey_l3_8b_v3.inference(task=l8_v3_combat_benchmark[i], reset_env=False, feedback_rounds=1)
        #         i += 1
        #         retry = MAX_RETRY
        #     except Exception as e:
        #         logger.critical(l8_v3_combat_benchmark[i]+' failed. retry...')
        #         logger.critical(e)
        #         traceback.print_exc()
        #         if retry > 0:
        #             retry -= 1
        #             continue
        #         i += 1
        #         retry = MAX_RETRY
        # i = 0
        # while i < len(multi_rounds_tasks):
        #     try:
        #         odyssey_l3_8b_v3.inference(task=multi_rounds_tasks[i], reset_env=False, feedback_rounds=3)
        #         i += 1
        #         retry = MAX_RETRY
        #     except Exception as e:
        #         logger.critical(multi_rounds_tasks[i]+' failed. retry...')
        #         logger.critical(e)
        #         traceback.print_exc()
        #         if retry > 0:
        #             retry -= 1
        #             continue
        #         i += 1
        #         retry = MAX_RETRY

def explore():
    odyssey_l3_8b = Odyssey(
        mc_port=mc_port,
        mc_host=mc_host,
        env_wait_ticks=env_wait_ticks,
        skill_library_dir="./skill_library",
        reload=True, # set to True if the skill_json updated
        embedding_dir=embedding_dir, # your model path
        environment='explore',
        resume=False,
        server_port=node_port,
        critic_agent_model_name = ModelType.LLAMA3_8B,
        comment_agent_model_name = ModelType.LLAMA3_8B,
        planner_agent_qa_model_name = ModelType.LLAMA3_8B,
        planner_agent_model_name = ModelType.LLAMA3_8B,
        action_agent_model_name = ModelType.LLAMA3_8B,
        username='bot'
    )
    odyssey_l3_8b_v3 = Odyssey(
        mc_port=mc_port,
        mc_host=mc_host,
        env_wait_ticks=env_wait_ticks,
        skill_library_dir="./skill_library",
        reload=True, # set to True if the skill_json updated
        embedding_dir=embedding_dir, # your model path
        environment='explore',
        resume=False,
        server_port=node_port,
        critic_agent_model_name = ModelType.LLAMA3_8B_V3,
        comment_agent_model_name = ModelType.LLAMA3_8B_V3,
        planner_agent_qa_model_name = ModelType.LLAMA3_8B_V3,
        planner_agent_model_name = ModelType.LLAMA3_8B_V3,
        action_agent_model_name = ModelType.LLAMA3_8B_V3,
        username='bot'
    )
    odyssey_l3_70b = Odyssey(
        mc_port=mc_port,
        mc_host=mc_host,
        env_wait_ticks=env_wait_ticks,
        skill_library_dir="./skill_library",
        reload=True, # set to True if the skill_json updated
        embedding_dir=embedding_dir, # your model path
        environment='explore',
        resume=False,
        server_port=node_port,
        critic_agent_model_name = ModelType.LLAMA3_70B_V1,
        comment_agent_model_name = ModelType.LLAMA3_70B_V1,
        planner_agent_qa_model_name = ModelType.LLAMA3_70B_V1,
        planner_agent_model_name = ModelType.LLAMA3_70B_V1,
        action_agent_model_name = ModelType.LLAMA3_70B_V1,
        username='bot'
    )
    # odyssey_l3_8b_v3.learn()
    odyssey_l3_8b.learn()
    # odyssey_l3_70b.learn()

def test_farming():
    odyssey_l3_8b = Odyssey(
        mc_port=mc_port,
        mc_host=mc_host,
        env_wait_ticks=env_wait_ticks,
        skill_library_dir="./skill_library",
        reload=True, # set to True if the skill_json updated
        embedding_dir=embedding_dir, # your model path
        environment='farming',
        resume=False,
        server_port=node_port,
        critic_agent_model_name = ModelType.LLAMA3_8B_V3,
        comment_agent_model_name = ModelType.LLAMA3_8B_V3,
        planner_agent_qa_model_name = ModelType.LLAMA3_8B_V3,
        planner_agent_model_name = ModelType.LLAMA3_8B_V3,
        action_agent_model_name = ModelType.LLAMA3_8B_V3,
    )
    odyssey_l3_70b = Odyssey(
        mc_port=mc_port,
        mc_host=mc_host,
        env_wait_ticks=env_wait_ticks,
        skill_library_dir="./skill_library",
        reload=True, # set to True if the skill_json updated
        embedding_dir=embedding_dir, # your model path
        environment='farming',
        resume=False,
        server_port=node_port,
        critic_agent_model_name = ModelType.LLAMA3_70B_V1,
        comment_agent_model_name = ModelType.LLAMA3_70B_V1,
        planner_agent_qa_model_name = ModelType.LLAMA3_70B_V1,
        planner_agent_model_name = ModelType.LLAMA3_70B_V1,
        action_agent_model_name = ModelType.LLAMA3_70B_V1,
    )
    farming_benchmark = [
                    "collect 1 seed (wheat or melon or pumpkin)",
                    "hoe a farmland",
                    "collect 1 wool by shearing 1 sheep",
                    "collect 1 bucket of milk",
                    "cook 1 meat (beef or mutton or pork or chicken)",
                    "obtain 1 leather",
                    "make 1 sugar",
                    "collect 1 bucket of water"
                    ]
    while True:
        # # for task in farming_benchmark:
        # i = 0
        # while i < len(farming_benchmark):
        #     try:
        #         odyssey_l3_70b.learn(goals=farming_benchmark[i], reset_env=False)
        #         i += 1
        #     except Exception as e:
        #         logger.critical(farming_benchmark[i]+' failed. retry...')
        #         logger.critical(e)
        #         traceback.print_exc()
        i = 0
        while i < len(farming_benchmark):
            try:
                odyssey_l3_8b.learn(goals=farming_benchmark[i], reset_env=False)
                i += 1
            except Exception as e:
                logger.critical(farming_benchmark[i]+' failed. retry...')
                logger.critical(e)
                traceback.print_exc()

def test_skill(skill_name):
    odyssey_skill = Odyssey(
        mc_port=mc_port,
        mc_host=mc_host,
        env_wait_ticks=env_wait_ticks,
        reload=True, # set to True if the skill_json updated
        embedding_dir=embedding_dir, # your model path
        resume=False,
        server_port=node_port,
    )
    odyssey_skill.run_raw_skill(f"./skill_library/skill/compositional/{skill_name}", skill_lib="old", reset=True)
    while True:
        odyssey_skill.run_raw_skill(f"./skill_library/skill/compositional/{skill_name}", reset=False)

def test_mc_skill(skill_name, para_list):
    odyssey_mc_skill = Odyssey(
        mc_port=mc_port,
        mc_host=mc_host,
        env_wait_ticks=env_wait_ticks,
        resume=False,
        server_port=node_port,
        username='bot'
    )
    odyssey_mc_skill.run_raw_skill(f"../MC-Comprehensive-Skill-Library/skill/{skill_name}", para_list, skill_lib="new", reset=True)
    while True:
        odyssey_mc_skill.run_raw_skill(f"../MC-Comprehensive-Skill-Library/skill/{skill_name}", para_list, skill_lib="new", reset=False)

if __name__ == '__main__':
    # Delete all the directories under the ckpt folder
    if os.path.exists('./ckpt'):
        for root, dirs, files in os.walk('./ckpt', topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))

    # Parse the id and task from the config.json
    task = config.get('TASK')
    id = config.get('ID')

    # Create required files under out folder
    if not os.path.exists("./out"):
        os.mkdir("./out")

    if not os.path.exists(f"./out/{task}"):
        os.mkdir(f"./out/{task}")

    open(f"./out/{task}/{task}_{id}_chat.log", "a").close()
    open(f"./out/{task}/{task}_{id}_inventory.log", "a").close()
    open(f"./out/{task}/{task}_{id}_move.log", "a").close()

    # test_mc_skill("obtainItem.js", [1, "diamond"])
    # test_subgoal()

    odyssey_l3_8b = Odyssey(
        mc_port=mc_port,
        mc_host=mc_host,
        env_wait_ticks=env_wait_ticks,
        skill_library_dir="./skill_library",
        reload=True,  # set to True if the skill_json updated
        embedding_dir=embedding_dir,  # your model path
        environment='farming',
        resume=False,
        server_port=node_port,
        critic_agent_model_name=ModelType.LLAMA3_8B_V3,
        comment_agent_model_name=ModelType.LLAMA3_8B_V3,
        planner_agent_qa_model_name=ModelType.LLAMA3_8B_V3,
        planner_agent_model_name=ModelType.LLAMA3_8B_V3,
        action_agent_model_name=ModelType.LLAMA3_8B_V3,
    )

    # odyssey_l3_8b.inference_sub_goal(task="subgoal_llama3_8b_v3", sub_goals=["mine diamond"])
    odyssey_l3_8b.learn(goals="Your final goal is to cook 1 meat (beef or mutton or pork or chicken).\n"
                              "Guidance:\n"
                              "1. There are four kinds of meat in Minecraft, beef, mutton, pork, and chicken.\n"
                              "2. You can obtain any of the meat and cook it to achieve the goal.\n"
                              "3. You can obtain the meat by killing the corresponding mob, i.e., cow, sheep, pig, and chicken.\n"
                              "4. Craft and place a furnace, and start cooking the meat once you obtain the meat.",
                        reset_env=False)

    # odyssey_l3_8b.learn(goals="Your final goal is to shear a sheep.\n"
    #                           "Guidance:\n"
    #                           "1. This task requires you to find a sheep and shear it.\n"
    #                           "2. To shear a sheep, you need to craft a shear first by using two iron ingots.",
    #                 reset_env=False)

    # odyssey_l3_8b = Odyssey(
    #     mc_port=mc_port,
    #     mc_host=mc_host,
    #     env_wait_ticks=env_wait_ticks,
    #     skill_library_dir="./skill_library",
    #     reload=True,  # set to True if the skill_json updated
    #     embedding_dir=embedding_dir,  # your model path
    #     environment='combat',
    #     resume=False,
    #     server_port=node_port,
    #     critic_agent_model_name=ModelType.LLAMA3_8B,
    #     comment_agent_model_name=ModelType.LLAMA3_8B,
    #     planner_agent_qa_model_name=ModelType.LLAMA3_8B,
    #     planner_agent_model_name=ModelType.LLAMA3_8B,
    #     action_agent_model_name=ModelType.LLAMA3_8B,
    # )
    #
    # odyssey_l3_8b.inference(task="1 skeleton", reset_env=False, feedback_rounds=1)


    # explore()